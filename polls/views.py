from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question

# Create your views here.
class IndexView(generic.ListView):
  template_name = "polls/index.html"
  # ListView의 경우 자동으로 생성되는 컨텍스트 변수는 question_list
  # 이것을 덮어 쓰려면 context_object_name 속성을 제공하고, 
  # 대신에 latest_question_list 를 사용하도록 지정
  context_object_name = "latest_question_list"

  def get_queryset(self):
    return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
  model = Question
  template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
  model = Question
  template_name = "polls/results.html"

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)

  try:
    selected_choice = question.choice_set.get(pk=request.POST["choice"])
  except (KeyError, Choice.DoesNotExist):
    # 만약 오류가 나면 다시 투표 창을 보여준다.
    return render(request, "polls/detail.html", {"question": question, "error_message": "You didn't select a choice.",},)
  
  else:
    selected_choice.votes += 1
    selected_choice.save()

  return HttpResponseRedirect(reverse("polls:results", args=(question.id, )))
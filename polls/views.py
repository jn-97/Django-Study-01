from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question

# Create your views here.
def index(request):
  latest_question_list = Question.objects.order_by("-pub_date")[:5]
  
  context = {
    "latest_question_list": latest_question_list,
  }

  return render(request, "polls/index.html", context)

def detail(request, question_id):
  # 만약 객체가 존재하지 않으면 Http404 예외 발생
  question = get_object_or_404(Question, pk=question_id)
  # 모든 객체를 가져오고 싶으면 => get_list_or_404

  return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
  response = "You're looking at the results of question %s."
  return HttpResponse(response % question_id)

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
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question

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
  return HttpResponse("You're voting on question %s." % question_id)
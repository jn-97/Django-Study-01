import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
  question_text = models.CharField(max_length=200) # 질문
  pub_date = models.DateTimeField("date published") # 발행일

  # __str__() => 객체의 표현을 대화식 프롬프트에서 편하게 보기 위해 사용
  # ex. python manage.py shell -> Question.objects.all()
  # <QuerySet [<Question: Question object (1)>]> -> <QuerySet [<Question: What's up?>]>
  def __str__(self):
    return self.question_text
  
  @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
  
  def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now

# 각각의 Choice가 하나의 Question에 관계됨
class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200) # 선택 텍스트
  votes = models.IntegerField(default=0) # 투표 집계

  def __str__(self):
    return self.choice_text
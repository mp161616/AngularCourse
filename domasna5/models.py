import random

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count, Sum, F, When, Case
from django.db.models.functions import Cast
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext as _


# Create your models here.

class CourseUser(models.Model):
    courseUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    hobbies = models.TextField(max_length=50)


class Quiz(models.Model):
    courseUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    number_of_questions = models.IntegerField()
    duration = models.IntegerField()  # in minutes
    required_score_to_pass = models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.TextField()
    correctAnswer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Question: {self.question.text}, Answer: {self.text}, Correct answer: {self.correctAnswer} "


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True, blank=True)
    courseUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)



class Section(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    text1 = models.TextField()
    header2 = models.CharField(max_length=50)
    text2 = models.TextField()
    subtext2 = models.TextField(null=True, blank=True)
    header3 = models.CharField(max_length=50)
    text3 = models.TextField()
    subtext3 = models.TextField(null=True, blank=True)
    photo = models.ImageField()

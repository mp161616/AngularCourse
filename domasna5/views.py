from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import NewUserForm
from .models import Quiz, CourseUser, Section  # , Section
from django.views.generic import ListView
from django.http import JsonResponse, Http404, HttpResponseRedirect


# Create your views here.


def home_view(request):
    quiz = Quiz.objects.all()
    return render(request, 'home.html', {'home': quiz})


def home_view1(request):
    quiz = Quiz.objects.all()
    return render(request, 'home1.html', {'home1': quiz})


def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'index.html', {'obj': quiz})


def quizMain_view(request):
    quiz = Quiz.objects.all()
    return render(request, 'main.html', {'obj': quiz})


def user_view(request):
    queryset1 = CourseUser.objects.filter(courseUser=request.user).all()
    return render(request, 'profile.html', {'profile': queryset1})


def courses_view(request):
    queryset1 = Quiz.objects.all()
    return render(request, 'courses.html', {'courses': queryset1})


def courses1_view(request):
    queryset1 = Quiz.objects.all()
    return render(request, 'courses1.html', {'courses1': queryset1})


def section_view(request, pk):
    queryset1 = Section.objects.get(pk=pk)
    return render(request, 'section.html', {'section': queryset1})


def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.duration
    })


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("payment")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def payment_view(request):
    quiz = Quiz.objects.all()
    return render(request, 'payment.html', {'payment': quiz})

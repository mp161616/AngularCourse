"""AngularCourse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from AngularCourse import settings
from domasna5.views import home_view, user_view, courses_view, \
    courses1_view, section_view, quizMain_view, quiz_data_view, quiz_view, home_view1, register_request, payment_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', home_view, name='home'),
    path('home/', home_view1, name='home1'),
    path('profile/', user_view, name='profile'),
    path('courses/', courses_view, name='courses'),
    path('courses1/', courses1_view, name='courses1'),
    path('main/', quizMain_view, name='mainQuiz'),
    path('section/<pk>/', section_view, name="section-view"),
    path('main/<pk>/', quiz_view, name='quiz-view'),
    path("register/", register_request, name="register"),
    # path('main/<pk>/save', save_quiz_view, name="save-quiz-view"),
    path('main/<pk>/data', quiz_data_view, name="quiz-data-view"),
    path('payment/', payment_view, name='payment'),



]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

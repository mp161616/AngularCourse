from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from domasna5.models import CourseUser


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

   # def save(self, commit=True):
    #    user = super(NewUserForm, self).save(commit=False)
     #   user.email = self.cleaned_data['email']
      #  if commit:
       #     user.save()
       # return user

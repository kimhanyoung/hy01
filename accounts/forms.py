from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    name = forms.CharField()
    company = forms.CharField()

    def save(self):
        user = super().save()
        profile = Profile.objects.create(
            user=user, phone_number=self.cleaned_data['phone_number'],
            company=self.cleaned_data['company'],
            name=self.cleaned_data['name'])
        return user


from django import forms
from django.forms import Textarea, TextInput
from shop.models import Category


class CategorySearchForm(forms.Form):
    search_word = forms.CharField(label='보험명 검색 ')







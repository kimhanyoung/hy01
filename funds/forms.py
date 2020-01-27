from django import forms

class FundSearchForm(forms.Form):
    search_word = forms.CharField(label='펀드명 검색')


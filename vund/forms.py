from django import forms
from django.forms import Textarea, TextInput
from vund.models import Ma000insu_list, Ma001fund_list
from django.forms.models import inlineformset_factory

class VundSearchForm(forms.Form):
    search_word = forms.CharField(label='보험명 검색 ')



VundInlineFormSet = inlineformset_factory(Ma000insu_list, Ma001fund_list,
    fields = ['fund_name', 'fund_code','create_date', 'fund_type02', 'input_percent'],
            extra = 1)


            # widgets={'fund_name' : TextInput(attrs={'cols':20 })
    #   })



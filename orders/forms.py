from django import forms
from .models import Order, Fund


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['entry_date',
                  'premium',
                  'paying_period',
                  'gender',
                  'present_age',
                  'pention_age',
                  'transfer_date',
                  'entry_method',
                  'risk_premium',
                  'count',
                  'payment',
                  'sign_charge7',
                  'sign_charge810',
                  'management_charge7',
                  'management_charge810',
                  'management_charge11',
                  'sign_charge1',
        ]


class FundForm(forms.ModelForm):       #펀드상세화면용
    class Meta:
        model = Fund
        fields = ('fund_name',)
        widgets = {
            'fund_name': forms.TextInput(attrs={'readonly': 'readonly'}),
        }


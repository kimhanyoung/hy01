from django import forms

class AddProductForm(forms.Form):
    quantity = forms.IntegerField(label='편입비율')
    is_update = forms.BooleanField(required=False, initial=True, widget=forms.HiddenInput)
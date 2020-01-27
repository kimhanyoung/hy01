from django import forms
from django.urls import reverse_lazy

from .models import Post

#class UploadFileForm(forms.ModelForm):
#    class Meta:
#        model = Post
#        fields = ('title', 'content')
#        initial = {'slug': 'auto-filling-do-not-input'}#

#    def __init__(self, *args, **kwargs):
#        super(UploadFileForm, self).__init__(*args, **kwargs)
#        self.fields['image'].required = False




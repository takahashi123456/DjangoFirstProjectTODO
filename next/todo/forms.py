
from django import forms
from .models import todoModel

class todoForm(forms.ModelForm):
    class Meta:
        model = todoModel
        fields = ['title',  'content','author','dateline', 'priority']
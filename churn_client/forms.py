from django import forms
from .models import ChurnModel

class ChurnForm(forms.ModelForm):
    class Meta:
        model = ChurnModel
        exclude = ['Churn']  

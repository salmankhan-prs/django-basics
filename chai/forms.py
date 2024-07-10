from django import forms

from .models import ChaiVariety



class  ChaiVarietyForms(forms.Form):
    chai_variety = forms.ModelMultipleChoiceField(queryset=ChaiVariety.objects.all(),label="Select chai variety ")
    
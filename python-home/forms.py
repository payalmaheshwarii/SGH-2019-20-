from django import forms
from home.models import patients


class patientsForm(forms.ModelForm):
    class Meta:
        model = patients
        fields = '__all__'
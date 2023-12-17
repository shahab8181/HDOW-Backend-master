from django import forms
from core.models import Case,Study,Echo

class NewCaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = "__all__"
        exclude = ['technician','reporting_md','status','related_study']

class NewStudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = "__all__"

class NewEchoForm(forms.ModelForm):
    class Meta:
        model = Echo
        fields = "__all__"
        # exclude = ['flagged',]
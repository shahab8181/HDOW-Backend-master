from django import forms
from core.models import User
from core.models import MedicalDoctor

class NewPatientForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['birthdate', 'gender', 'phone', 'address']
        exclude = ['account']

class NewDoctorForm(forms.ModelForm):
    class Meta:
        model = MedicalDoctor
        fields = "__all__"
        exclude = ['account']
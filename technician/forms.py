from django import forms
from technician.models import Technician

class NewTechnicianForm(forms.ModelForm):
    class Meta:
        model = Technician
        fields = "__all__"
        exclude = ['account']
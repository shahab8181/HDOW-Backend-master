from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# from client.models import Client
from client.forms import NewPatientForm,NewDoctorForm
from core.models import Case,User,MedicalDoctor
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.db import transaction
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import ClientSerializer



class Client_api(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ClientSerializer






class PatientsListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = User
    template_name = 'client/patients.html'
    context_object_name = 'patients'
    paginate_by = 10
    login_url = 'login'
    permission_required = 'client.view_client'

    def get_context_data(self, **kwargs):
        context = super(PatientsListView,self).get_context_data(**kwargs)
        context['title'] = 'Patients'
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        return context

class PatientDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView,UpdateView):
    model = User
    context_object_name = 'patient'
    template_name = 'client/patientdetail.html'
    permission_required = ['client.edit_client','client.view_client']
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView,self).get_context_data(**kwargs)
        context['title'] = self.object
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        return context

class NewPatientView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):

        form_class = NewPatientForm
        model = User
        template_name = 'client/newpatient.html'
        permission_required = 'client.add_client'

        def get_context_data(self, **kwargs):
            context = super(NewPatientView,self).get_context_data(**kwargs)
            context['title'] = 'New Patient'
            context['new_cases_count'] = Case.objects.filter(status=1).count()
            return context

        @transaction.atomic
        def form_valid(self,form):

            try:
                patient = form.save(commit=False)
                # patient.account = User.objects.create_user(
                #     first_name=self.request.POST.get('first_name'),
                #     last_name=self.request.POST.get('last_name'),
                #     email=self.request.POST.get('email'),
                #     username=self.request.POST.get('email'),
                #     password=self.request.POST.get('password'),
                #     role=3
                # )
                patient.save()
                return super().form_valid(form)

            except IntegrityError:
                return render(self.request,'client/newpatient.html',{"error":"User Email Must be Unique"})


        def get_success_url(self):
            return reverse('patients')


class DoctorsListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = MedicalDoctor
    template_name = 'client/doctors.html'
    context_object_name = 'doctors'
    paginate_by = 10
    login_url = 'login'
    permission_required = 'core.add_medicaldoctor'

    def get_context_data(self, **kwargs):
        context = super(DoctorsListView,self).get_context_data(**kwargs)
        context['title'] = 'Doctors'
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        return context

class NewDoctorView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):

        form_class= NewDoctorForm
        model=MedicalDoctor
        template_name='client/newdoctor.html'
        permission_required = 'core.add_medicaldoctor'

        def get_context_data(self, **kwargs):
            context = super(NewDoctorView,self).get_context_data(**kwargs)
            context['title'] = 'New Doctor'
            context['new_cases_count'] = Case.objects.filter(status=1).count()
            return context

        @transaction.atomic
        def form_valid(self,form):
            doctor = form.save(commit=False)
            doctor.account = User.objects.create_user(
                first_name=self.request.POST.get('first_name'),
                last_name=self.request.POST.get('last_name'),
                email=self.request.POST.get('email'),
                username=self.request.POST.get('email'),
                password=self.request.POST.get('password'),
                role=4
            )
            doctor.save()
            return super().form_valid(form)

        def get_success_url(self):
            return reverse('doctors')
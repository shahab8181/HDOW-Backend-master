from django.urls import path
from client.views import PatientsListView,NewPatientView,PatientDetailView,DoctorsListView,NewDoctorView, Client_api


urlpatterns = [
    # Patient
    path('patients/',PatientsListView.as_view(),name='patients'),
    path('patients/new',NewPatientView.as_view(),name='new_patient'),
    path('patients/<pk>',PatientDetailView.as_view(),name='patientdetail'),

    # Doctor
    path('doctors/',DoctorsListView.as_view(),name='doctors'),
    path('doctors/new',NewDoctorView.as_view(),name='new_doctor'),

    # TODO: api views
    path('client/api', Client_api.as_view()),
]
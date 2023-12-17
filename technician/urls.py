from django.urls import path
from core.views import CaseListView
from technician.views import TechnicianListView,NewTechnicianView , Technician_api

urlpatterns = [
    path('',TechnicianListView.as_view(),name='technicians'),
    path('dashboard/',CaseListView.as_view(),name='technician_dashboard'),
    path('new/',NewTechnicianView.as_view(),name='new_technician'),

    # TODO: api views
    path('api/', Technician_api.as_view()),
]
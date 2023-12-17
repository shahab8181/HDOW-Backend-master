from django.urls import path
from supervisor.views import SupervisorDashboardView, Supervisor_api

urlpatterns = [
    path('dashboard/',SupervisorDashboardView,name='supervisor_dashboard'),

    # TODO: api views
    path('api/', Supervisor_api.as_view()),
]
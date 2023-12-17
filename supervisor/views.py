from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from core.models import Case
# from client.models import Client
from rest_framework.generics import ListCreateAPIView
from .models import Supervisor
from .serializers import SupervisorSerializer
from core.models import User

class Supervisor_api(ListCreateAPIView):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer


@login_required(login_url='login')
def SupervisorDashboardView(request):
    if request.user.role==2 or request.user.is_superuser:
        cases = Case.objects.filter(status=1)
        context={'title':'Dashboard',
        'name':request.user.first_name,
        'new_cases_count': cases.count(),
        'role': request.user.role,
        'latest_cases': cases.order_by('-created_at')[:5],
        'client_count': User.objects.all().count()
        }
        return render(request,'supervisor/dashboard.html',context=context)
    else:
        raise PermissionDenied()
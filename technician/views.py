from core.models import User,Case
from technician.models import Technician
from technician.forms import NewTechnicianForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.db import transaction
from django.urls import reverse
from rest_framework.generics import ListCreateAPIView
from .serializers import TechnicianSerializer



class Technician_api(ListCreateAPIView):
    queryset = Technician.objects.all()
    serializer_class = TechnicianSerializer




class TechnicianListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model = Technician
    paginate_by = 10
    template_name = 'technician/technicians.html'
    context_object_name = 'technicians'
    login_url = 'login'
    permission_required = 'technician.view_technician'

    def get_context_data(self, **kwargs):
        context = super(TechnicianListView,self).get_context_data(**kwargs)
        context['title'] = 'Technicians'
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        context['role'] = self.request.user.role        
        return context

class NewTechnicianView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):

        form_class = NewTechnicianForm
        model = Technician
        template_name = 'technician/newtechnician.html'
        permission_required = 'technician.add_technician'

        def get_context_data(self, **kwargs):
            context = super(NewTechnicianView,self).get_context_data(**kwargs)
            context['title'] = 'New Technician'
            context['new_cases_count'] = Case.objects.filter(status=1).count()
            return context

        @transaction.atomic
        def form_valid(self,form):
            patient = form.save(commit=False)
            patient.account = User.objects.create_user(
                first_name=self.request.POST.get('first_name'),
                last_name=self.request.POST.get('last_name'),
                email=self.request.POST.get('email'),
                username=self.request.POST.get('email'),
                password=self.request.POST.get('password'),
                role=1
            )
            patient.save()
            return super().form_valid(form)


        def get_success_url(self):
            return reverse('technicians')
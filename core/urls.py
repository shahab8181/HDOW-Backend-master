from django.urls import path
from core.views import (
    RedirectToDashboard,LoginView,LogoutView,
    CaseListView,NewCaseView,CaseDetailView,
    settings_view,EchoListView,NewEchoView,
    EchoDetailView, users_api, echos_api,
    studies_api, TWaveMorphologyOptions_api, StudyQualityOptions_api, Cases_api, StSegmentElevation_api, StSegmentDepression_api,
    Location_api, StSegmentOptions_api, MedicalDoctor_api, TimeStamp_api, Login_api
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Primary Paths
    path('',RedirectToDashboard,name='home'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('settings/',settings_view,name='settings'),

    # Secondary Paths
    path('cases/',CaseListView.as_view(),name='cases'),
    path('cases/new',NewCaseView.as_view(),name='newcase'),
    path('cases/<pk>',CaseDetailView.as_view(),name='casedetail'),

    path('echos/',EchoListView.as_view(),name='echos'),
    path('echos/new',NewEchoView.as_view(),name='newecho'),
    path('echos/<pk>',EchoDetailView.as_view(),name='echodetail'),



    # TODO: api views
    path('login/api/', Login_api.as_view(), name='api-login'),
    path('users/api/', users_api.as_view(), name='users-api'),
    path('MedicalDoctors/api/', MedicalDoctor_api.as_view()),
    path('TimeStamp/api/', TimeStamp_api.as_view()),
    path('TWaveMorphologyOptions/api/', TWaveMorphologyOptions_api.as_view()),
    path('StSegmentOptions/api/', StSegmentOptions_api.as_view()),
    path('StudyQualityOptions/api/', StudyQualityOptions_api.as_view()),
    path('StSegmentElevation/api/', StSegmentElevation_api.as_view()),
    path('StSegmentDepression/api/', StSegmentDepression_api.as_view()),
    path('locations/api/', Location_api.as_view()),
    path('studies/api/', studies_api.as_view()),
    path('cases/api/', Cases_api.as_view()),
    path('echos/api/', echos_api.as_view(), name='echos-api'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from .models import User, TimeStamp, MedicalDoctor, Study,\
    Case, TWaveMorphologyOptions, StSegmentOptions, StudyQualityOptions,\
    StSegmentElevation, StSegmentDepression, Location, Echo
# Register your models here.


admin.site.register(User)
admin.site.register(TimeStamp)
admin.site.register(MedicalDoctor)
admin.site.register(Study)
admin.site.register(Case)
admin.site.register(TWaveMorphologyOptions)
admin.site.register(StSegmentOptions)
admin.site.register(StudyQualityOptions)
admin.site.register(StSegmentDepression)
admin.site.register(StSegmentElevation)
admin.site.register(Location)
admin.site.register(Echo)
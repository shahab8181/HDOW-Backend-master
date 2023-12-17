from rest_framework import serializers
from .models import User, Echo, Study, StudyQualityOptions, TWaveMorphologyOptions, Case, StSegmentOptions, StSegmentElevation, StSegmentDepression, Location, TimeStamp, MedicalDoctor
from technician.serializers import TechnicianSerializer




class TimeStampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeStamp
        fields = '__all__'


class TWaveMorphologyOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = TWaveMorphologyOptions
        fields = '__all__'

class StudyQualityOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyQualityOptions
        fields = '__all__'



class StSegmentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StSegmentOptions
        fields = '__all__'



class StSegmentElevationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StSegmentElevation
        fields = '__all__'



class StSegmentDepressionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StSegmentDepression
        fields = '__all__'







class StudySerializer(serializers.ModelSerializer):
    # StudyQualityOptions_set = StudyQualityOptionsSerializer(read_only=True, many=True)

    class Meta:
        model = Study
        fields = '__all__'




class CaseSerializer(serializers.ModelSerializer):
    # related_client = UserSerializer(read_only=True, many=True)
    # related_technician = UserSerializer(read_only=True, many=True)
    # reporting_md_set = MedicalDoctorSerializer(read_only=True, many=True)
    # referring_md = MedicalDoctorSerializer(read_only=True, /many=True)
    # related_study_set = StudySerializer(read_only=True, many=True)

    class Meta:
        model = Case
        fields = '__all__'




class EchoSerializer(serializers.ModelSerializer):
    # account_set = UserSerializer(read_only=True, many=True)
    # echo_referring_md = MedicalDoctorSerializer(read_only=True, many=True)
    # location_set = LocationSerializer(read_only=True, many=True)
    # stsegment_options = StSegmentOptionsSerializer(read_only=True, many=True)
    # st_segment = StSegmentElevationSerializer(read_only=True, many=True)
    # st_segment = StSegmentDepressionSerializer(read_only=True, many=True)
    # t_wave_morphology_set = TWaveMorphologyOptionsSerializer(read_only=True, many=True)

    class Meta:
        model = Echo
        fields = '__all__'
from core.models import User
User.is_superuser

class LocationSerializer(serializers.ModelSerializer):
    # location_set = EchoSerializer(read_only=True, many=True)

    class Meta:
        model = Location
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # echos = EchoSerializer(read_only=True, many=True)
    # cases = CaseSerializer(read_only=True, many=True)
    # case_technicians = CaseSerializer(read_only=True, many=True)
    # technicians = TechnicianSerializer(read_only=True, many=True)
    # account = MedicalDoctorSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'password', 'first_name',
            'last_name', 'age', 'birthdate', 'gender', 'phone', 'address'
            # 'cases', 
            # 'case_technicians', 'technicians',
            # 'account'
        ]




class MedicalDoctorSerializer(serializers.ModelSerializer):
    # account_set = UserSerializer(read_only=True, many=True)
    # reporting_md_set = 
    # reporting_md_set = CaseSerializer(read_only=True, many=True)
    # referring_md = CaseSerializer(read_only=True, many=True)

    class Meta:
        model = MedicalDoctor
        fields = '__all__'



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
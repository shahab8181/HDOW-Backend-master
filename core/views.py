from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView
from django.core.exceptions import PermissionDenied,ValidationError
from core.utils import Flagger,EchoFlagger
from django.urls import reverse
from core.models import User,Case,MedicalDoctor,Study,Echo,TWaveMorphologyOptions,StSegmentOptions
from core.forms import NewCaseForm,NewStudyForm,NewEchoForm
# from client.models import Client
from django.http import HttpResponseRedirect
from core.models import MedicalDoctor,StudyQualityOptions,StSegmentElevation,StSegmentDepression,Location

from rest_framework.generics import ListCreateAPIView, GenericAPIView
from .serializers import (UserSerializer, StudySerializer,EchoSerializer, StSegmentOptionsSerializer,
                          StudyQualityOptionsSerializer, TWaveMorphologyOptionsSerializer, CaseSerializer, 
                        StSegmentElevationSerializer, StSegmentDepressionSerializer, LocationSerializer, MedicalDoctorSerializer, TimeStampSerializer
)
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import TimeStamp
from django.contrib.auth import login
# TODO: api views
import json
from .models import Study
# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .models import User
from .serializers import UserSerializer, LoginSerializer
from os  import system
from django.contrib.auth.hashers import check_password
import time
from urllib import parse
# class Login_api(APIView):
#     def post(self, request: Request, *args, **kwargs):
#         ser = LoginSerializer(data=request.data)

#         username = request.data.get('username')
#         password = request.data.get('password')
#         system('cls')
#         print(username)
#         print(password)
#         if username and password:
#             user_exists = User.objects.filter(username__iexact=username).exists()
#             if user_exists:
#                 print(username)
#                 print(password)
#                 check_password = check_password(password)
#                 if check_password:
#                     return Response({'id': user_exists.id}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'message': 'Invalid username or password'}, status=400)
#         else:
#             return Response({'message': request.data}, status=400)


class Login_api(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = LoginSerializer


    def post(self, request: Request, *args, **kwargs):
        user = User.objects.filter(username=request.data.get('username')).first()
        if user.check_password(request.data.get('password')):
            login(request, user)
            return Response({
              'id': user.id,
              'first_name': user.first_name,
              'last_name': user.last_name
            }, status=status.HTTP_200_OK)
        return Response({'status': 'username or password incorect'}, status=status.HTTP_200_OK)
        



# class Login_api(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = LoginSerializer
    
#     def pos

class users_api(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        user = User.objects.all()
        serializer = UserSerializer(instance=user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request: Request, *args, **kwargs):
        # data = request.data.get('UserData', {})

        # try:
        #     data = json.loads(data)
        # except json.JSONDecodeError as e:
        #     return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = User()
            # new_user.id = serializer.validated_data.get('id')
            new_user.username = serializer.validated_data.get('username')
            new_user.set_password(serializer.validated_data.get('password'))
            new_user.first_name = serializer.validated_data.get('first_name')
            new_user.last_name = serializer.validated_data.get('last_name')
            new_user.age = serializer.validated_data.get('age')
            new_user.birthdate = serializer.validated_data.get('birthdate')
            new_user.gender = serializer.validated_data.get('gender')
            new_user.phone = serializer.validated_data.get('phone')
            new_user.address = serializer.validated_data.get('address')
            new_user.save()

            return Response({'id': new_user.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicalDoctor_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        md = MedicalDoctor.objects.all()
        serializer = MedicalDoctorSerializer(instance=md, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('MedicalDoctorData', {})

        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = MedicalDoctorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimeStamp_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        ts = TimeStamp.objects.all()
        serializer = TimeStampSerializer(instance=ts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('TimeStampData', {})

        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TimeStampSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class studies_api(APIView):
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        study = Study.objects.all()
        serializer = StudySerializer(instance=study, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        urlencoded = request.data.get('EchoData', {})
        to_parse = parse.unquote(urlencoded)
        to_dic = json.loads(to_parse) # json to dictionary
        json_value = to_dic.get('study_quality')
            
        to_list = []

        for char in json_value:
            if char.isdigit():
                to_list.append(char)
        else:
            final_value = list(map(int, to_list))
            to_dic['study_quality'] = final_value
            data = json.dumps(to_dic)

        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = StudySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Cases_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        case = Case.objects.all()
        serializer = CaseSerializer(instance=case, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('CaseData', {})
        
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CaseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TWaveMorphologyOptions_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        tmo = TWaveMorphologyOptions.objects.all()
        serializer = TWaveMorphologyOptionsSerializer(instance=tmo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('TWMOData', {})
        
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TWaveMorphologyOptionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StSegmentOptions_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        sso = StSegmentOptions.objects.all()
        serializer = StSegmentOptionsSerializer(instance=sso, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('SSOData', {})
        
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StSegmentOptionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StudyQualityOptions_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        sqo = StudyQualityOptions.objects.all()
        serializer = StudyQualityOptionsSerializer(instance=sqo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('SQOData', {})
        
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StudyQualityOptionsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StSegmentElevation_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        sse = StSegmentElevation.objects.all()
        serializer = StSegmentElevationSerializer(instance=sse, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('SSEData', {})
        
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StSegmentElevationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class StSegmentDepression_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        ssd = StSegmentDepression.objects.all()
        serializer = StSegmentDepressionSerializer(instance=ssd, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('SSDData', {})
        
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = StSegmentDepressionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class Location_api(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        location = Location.objects.all()
        serializer = LocationSerializer(instance=location, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        data = request.data.get('LocationData', {})
        
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LocationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class echos_api(APIView):
    # authentication_classes = [BasicAuthentication]
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        echo = Echo.objects.all()
        serializer = EchoSerializer(instance=echo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request, *args, **kwargs):
        # data = request.data.get('EchoData', {})
        urlencoded = request.data.get('EchoData', {})
        to_parse = parse.unquote(urlencoded)
        data = json.loads(to_parse) # json to dictionary
        system('cls')
        json_value_1 = data.get('location') # 1 to 12
        json_value_2 = data.get('st_segment') # 1 to 3
        json_value_3 = data.get('st_segment_depression') # 1 to 12
        json_value_4 = data.get('st_segment_elevation') # 1 to 12
        json_value_5 = data.get('t_wave_morphology') # 1 & 2

        to_list_1 = []
        to_list_2 = []
        to_list_3 = []
        to_list_4 = []
        to_list_5 = []

        if '10' in json_value_1 or '11' in json_value_1 or '12' in json_value_1:
            if '10' in json_value_1:
                to_list_1.append(int(json_value_1[json_value_1.find('10'):json_value_1.find('10')+2]))
                json_value_1 = json_value_1.replace(json_value_1[json_value_1.find('10'):json_value_1.find('10')+2], 'x')

            if '11' in json_value_1:
                to_list_1.append(int(json_value_1[json_value_1.find('11'):json_value_1.find('11')+2]))
                json_value_1 = json_value_1.replace(json_value_1[json_value_1.find('11'):json_value_1.find('11')+2], 'x')


            if '12' in json_value_1:
                to_list_1.append(int(json_value_1[json_value_1.find('12'):json_value_1.find('12')+2]))
                json_value_1 = json_value_1.replace(json_value_1[json_value_1.find('12'):json_value_1.find('12')+2], 'x')
         

            for char in json_value_1:
                if char.isdigit():
                    to_list_1.append(char)
            else:
                final_value_1 = list(map(int, to_list_1))
                data['location'] = final_value_1
        else:
            for char in json_value_1:
                if char.isdigit():
                    to_list_1.append(char)
            else:
                final_value = list(map(int, to_list_1))
                data['location'] = final_value
            
        
        for char in json_value_2:
            if char.isdigit():
                to_list_2.append(char)
        else:
            final_value = list(map(int, to_list_2))
            data['st_segment'] = final_value


        if '10' in json_value_3 or '11' in json_value_3 or '12' in json_value_3:
            if '10' in json_value_3:
                to_list_3.append(int(json_value_3[json_value_3.find('10'):json_value_3.find('10')+2]))
                json_value_3 = json_value_3.replace(json_value_3[json_value_3.find('10'):json_value_3.find('10')+2], 'x')

            if '11' in json_value_3:
                to_list_3.append(int(json_value_3[json_value_3.find('11'):json_value_3.find('11')+2]))
                json_value_3 = json_value_3.replace(json_value_3[json_value_3.find('11'):json_value_3.find('11')+2], 'x')


            if '12' in json_value_3:
                to_list_3.append(int(json_value_3[json_value_3.find('12'):json_value_3.find('12')+2]))
                json_value_3 = json_value_3.replace(json_value_3[json_value_3.find('12'):json_value_3.find('12')+2], 'x')
         

            for char in json_value_3:
                if char.isdigit():
                    to_list_3.append(char)
            else:
                final_value_1 = list(map(int, to_list_3))
                data['st_segment_depression'] = final_value_1
        else:
            for char in json_value_3:
                if char.isdigit():
                    to_list_3.append(char)
            else:
                final_value_1 = list(map(int, to_list_3))
                data['st_segment_depression'] = final_value_1


        if '10' in json_value_4 or '11' in json_value_4 or '12' in json_value_4:
            if '10' in json_value_4:
                to_list_4.append(int(json_value_4[json_value_4.find('10'):json_value_4.find('10')+2]))
                json_value_4 = json_value_4.replace(json_value_4[json_value_4.find('10'):json_value_4.find('10')+2], 'x')

            try:
                if '11' in json_value_4:
                    to_list_4.append(int(json_value_4[json_value_4.find('11'):json_value_4.find('11')+2]))
                    json_value_4 = json_value_4.replace(json_value_4[json_value_4.find('11'):json_value_4.find('11')+2], 'x')
            except:
                pass

            try:
                if '12' in json_value_4:
                    to_list_4.append(int(json_value_4[json_value_4.find('12'):json_value_4.find('12')+2]))
                    json_value_4 = json_value_4.replace(json_value_4[json_value_4.find('12'):json_value_4.find('12')+2], 'x')
            except:
                pass

            for char in json_value_4:
                if char.isdigit():
                    to_list_4.append(char)
            else:
                final_value_2 = list(map(int, to_list_4))
                data['st_segment_elevation'] = final_value_2
        else:
            for char in json_value_4:
                if char.isdigit():
                    to_list_4.append(char)
            else:
                final_value_2 = list(map(int, to_list_4))
                data['st_segment_elevation'] = final_value_2


        for char in json_value_5:
            if char.isdigit():
                to_list_5.append(char)
        else:
            final_value = list(map(int, to_list_5))
            data['t_wave_morphology'] = final_value

        data = json.dumps(data)

        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = EchoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return Response(serializer.validated_data.get('st_segment_elevation'), status=status.HTTP_400_BAD_REQUEST)





































# class echos_api(APIView):
#     # authentication_classes = [BasicAuthentication]
#     # authentication_classes = [SessionAuthentication, BasicAuthentication]
#     # permission_classes = [AllowAny]

#     def get(self, request, *args, **kwargs):
#         echo = Echo.objects.all()
#         serializer = EchoSerializer(instance=echo, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
#     def post(self, request, *args, **kwargs):
#         # data = request.data.get('EchoData', {})
#         urlencoded = request.data.get('EchoData', {})
#         to_parse = parse.unquote(urlencoded)
#         data = json.loads(to_parse) # json to dictionary
#         system('cls')
#         json_value_1 = data.get('location')
#         json_value_2 = data.get('st_segment')
#         json_value_3 = data.get('st_segment_depression')
#         json_value_4 = data.get('st_segment_elevation')
#         json_value_5 = data.get('t_wave_morphology')

#         to_list_1 = []
#         to_list_2 = []
#         to_list_3 = []
#         to_list_4 = []
#         to_list_5 = []

#         for char in json_value_1:
#             if char.isdigit():
#                 to_list_1.append(char)
#         else:
#             final_value = list(map(int, to_list_1))
#             data['location'] = final_value
        
        
#         for char in json_value_2:
#             if char.isdigit():
#                 to_list_2.append(char)
#         else:
#             final_value = list(map(int, to_list_2))
#             data['st_segment'] = final_value

#         if '10' in json_value_3 or '11' in json_value_3 or '12' in json_value_3:
#             if '10' in json_value_3:
#                 to_list_3.append(int(json_value_3[json_value_3.find('10'):json_value_3.find('10')+2]))
#                 json_value_3 = json_value_3.replace(json_value_3[json_value_3.find('10'):json_value_3.find('10')+2], 'x')

#             if '11' in json_value_3:
#                 to_list_3.append(int(json_value_3[json_value_3.find('11'):json_value_3.find('11')+2]))
#                 json_value_3 = json_value_3.replace(json_value_3[json_value_3.find('11'):json_value_3.find('11')+2], 'x')


#             if '12' in json_value_3:
#                     to_list_3.append(int(json_value_3[json_value_3.find('12'):json_value_3.find('12')+2]))
#                     json_value_3 = json_value_3.replace(json_value_3[json_value_3.find('12'):json_value_3.find('12')+2], 'x')
         

#             for char in json_value_3:
#                 if char.isdigit():
#                     to_list_3.append(char)
#             else:
#                 final_value_1 = list(map(int, to_list_3))
#                 data['st_segment_depression'] = final_value_1


#         if '10' in json_value_4 or '11' in json_value_4 or '12' in json_value_4:
#             if '10' in json_value_4:
#                 to_list_4.append(int(json_value_4[json_value_4.find('10'):json_value_4.find('10')+2]))
#                 json_value_4 = json_value_4.replace(json_value_4[json_value_4.find('10'):json_value_4.find('10')+2], 'x')

#             try:
#                 if '11' in json_value_4:
#                     to_list_4.append(int(json_value_4[json_value_4.find('11'):json_value_4.find('11')+2]))
#                     json_value_4 = json_value_4.replace(json_value_4[json_value_4.find('11'):json_value_4.find('11')+2], 'x')
#             except:
#                 pass

#             try:
#                 if '12' in json_value_4:
#                     to_list_4.append(int(json_value_4[json_value_4.find('12'):json_value_4.find('12')+2]))
#                     json_value_4 = json_value_4.replace(json_value_4[json_value_4.find('12'):json_value_4.find('12')+2], 'x')
#             except:
#                 pass

#             for char in json_value_4:
#                 if char.isdigit():
#                     to_list_4.append(char)
#             else:
#                 final_value_2 = list(map(int, to_list_4))
#                 data['st_segment_elevation'] = final_value_2


#         for char in json_value_5:
#             if char.isdigit():
#                 to_list_5.append(char)
#         else:
#             final_value = list(map(int, to_list_5))
#             data['t_wave_morphology'] = final_value

#         data = json.dumps(data)

#         try:
#             data = json.loads(data)
#         except json.JSONDecodeError as e:
#             return Response({'error': 'Invalid JSON format'}, status=status.HTTP_400_BAD_REQUEST)

#         serializer = EchoSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             # return Response(serializer.validated_data.get('st_segment_elevation'), status=status.HTTP_400_BAD_REQUEST)




















@login_required(login_url='login')
def RedirectToDashboard(request):
    _role = request.user.role
    if _role==1:
        return redirect('technician_dashboard')
    elif _role==2 or request.user.is_superuser:
        return redirect('supervisor_dashboard')
    elif _role==3:
        return redirect('client_dashboard')
    else:
        raise PermissionDenied()

class LoginView(LoginView):
    redirect_authenticated_user=True
    next_page = 'home'

class LogoutView(LogoutView):
    next_page = 'login'

class CaseListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=Case
    paginate_by=10
    template_name='core/cases.html'
    context_object_name = 'cases'
    login_url = 'login'
    permission_required = 'core.view_case'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(CaseListView,self).get_context_data(**kwargs)
        context['title'] = 'Echocardiographies'
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        context['studies'] = Study.objects.all()
        context['role'] = self.request.user.role
        
        
        return context

class NewCaseView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    form_class= NewCaseForm
    model=Case
    template_name='core/newcase.html'
    permission_required = 'core.add_case'


    def get_context_data(self, **kwargs):
        context = super(NewCaseView,self).get_context_data(**kwargs)
        context['title'] = 'New Echocardiography'
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        context['role'] = self.request.user.role
        # context['patients'] = User.objects.values('first_name','last_name','id')
        context['patients'] = User.objects.all()
        context['study'] = Study
        context['case'] = Case
        context['study_quality_options'] = StudyQualityOptions.objects.all()

        return context
    
    def form_valid(self, form):
        case = form.save(commit=False)
        flagger = Flagger()
        flagger = flagger.run(obj=self.request.POST, gender=case.client.gender)
        new_study = NewStudyForm(self.request.POST)
        new_study_instance = new_study.save(commit=False)
        new_study_instance.flagged = flagger.flagged
        new_study_instance.flagged_fields = flagger.flagged_fields

        case.technician = User.objects.get(pk=self.request.user.id)
        case.related_study = new_study_instance
        new_study_instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('casedetail',kwargs={'pk':self.object.pk})

class CaseDetailView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Case
    context_object_name = 'case'
    template_name = 'core/casedetail.html'
    permission_required = ['core.view_case','core.edit_case']
    fields = ['reporting_md','referring_md']

    def post(self,request,**kwargs):
        case = Case.objects.get(pk=self.kwargs['pk'])
        reporting_md = request.POST.get('reporting_md')
        referring_md = request.POST.get('referring_md')
        if reporting_md:
            case.reporting_md = MedicalDoctor.objects.get(pk=reporting_md)
            case.status = 3

            if referring_md:
                case.referring_md = MedicalDoctor.objects.get(pk=referring_md)

            case.save()
            return HttpResponseRedirect(reverse('casedetail',kwargs={'pk':self.kwargs['pk']}))

        if referring_md:
            case.referring_md = MedicalDoctor.objects.get(pk=referring_md)
            case.save()
            return HttpResponseRedirect(reverse('casedetail', kwargs={'pk': self.kwargs['pk']}))


    def get_context_data(self, **kwargs):
        context = super(CaseDetailView,self).get_context_data(**kwargs)
        context['title'] = self.object
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        context['doctors'] = MedicalDoctor.objects.all()
        # d = Case.objects.filter(related_study__id=self.kwargs.get('pk')).first()
        # context['study'] = d.related_study
        context['study'] = Study.objects.filter(id=self.kwargs.get('pk')).first()

        return context


    def get_success_url(self):
        return reverse('casedetail',kwargs={'pk':self.object.pk})


@login_required(login_url='login')
def settings_view(request):
    return render(request,'core/settings.html')

class EchoListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    model=Echo
    paginate_by=10
    template_name='echo/echos.html'
    context_object_name = 'echos'
    login_url = 'login'
    permission_required = 'core.view_echo'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        context = super(EchoListView,self).get_context_data(**kwargs)
        context['title'] = 'Electrocardiograms'
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        context['role'] = self.request.user.role

        return context

class NewEchoView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    form_class= NewEchoForm
    model=Case
    template_name='echo/newecho.html'
    permission_required = 'core.add_echo'

    def get_context_data(self, **kwargs):
        context = super(NewEchoView,self).get_context_data(**kwargs)
        context['title'] = 'New Electrocardiogram'
        context['patients'] = User.objects.values('first_name', 'last_name', 'id')
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        context['role'] = self.request.user.role
        context['echo'] = Echo
        context['morphologyoptions'] = TWaveMorphologyOptions.objects.all()
        context['referring_md'] = MedicalDoctor.objects.all()
        context['st_segment_options'] = StSegmentOptions.objects.all()
        context['st_segment_elevation_options'] = StSegmentElevation.objects.all()
        context['st_segment_depression_options'] = StSegmentDepression.objects.all()
        context['location_options'] = Location.objects.all()

        return context

    def form_valid(self, form):
        echo = form.save(commit=False)

        flagger = EchoFlagger()
        flagger = flagger.run(obj=self.request.POST)
        echo.flagged = flagger.flagged
        echo.flagged_fields = flagger.flagged_fields

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('echodetail',kwargs={'pk':self.object.pk})

class EchoDetailView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    model = Echo
    context_object_name = 'echo'
    template_name = 'echo/echodetail.html'
    permission_required = ['core.view_echo','core.edit_echo']
    fields = "__all__"

    def get_context_data(self, **kwargs):
        context = super(EchoDetailView,self).get_context_data(**kwargs)
        context['title'] = self.object
        context['new_cases_count'] = Case.objects.filter(status=1).count()
        context['doctors'] = MedicalDoctor.objects.all()

        return context

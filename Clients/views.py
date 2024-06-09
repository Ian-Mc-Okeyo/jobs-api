from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from .models import *
from knox.models import AuthToken
from django.contrib.auth import authenticate

class RegisterClient(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            #save the user
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()

            #create payment profile
            newPayment = Payment(user=user)
            newPayment.save()
            newProfile = UserProfile(user=user)
            newProfile.save()
            data = {
                'user': serializer.data,
                'token': AuthToken.objects.create(user)[1],
            }

            return Response(data, status=201)
        return Response(serializer.errors, status=400)

class ClientLogin(APIView):
    def post(self, request, *args, **kwargs):
        user = authenticate(password = request.data['password'], username=request.data['username'])
        payment = Payment.objects.filter(user=user).first()
        if user and payment:
            serializer = UserSerializer(user)
            data = {
                'user': serializer.data,
                'payment_status': payment.status,
                'token': AuthToken.objects.create(user)[1],
            }
            return Response(data, status=200)
        return Response({'Msg': 'Invalid credentials'}, status=404)

class ComapnyCreateUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            company = serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PostJob(APIView):
    def post(self, request, id, *args, **kwargs):
        company = Company.objects.filter(user__id=id).first()
        if not company:
            return Response({'Msg': 'Company not found'}, 404)
        request.data['company'] = company.id
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class GetJobs(APIView):
    def get(self, request, *args, **kwargs):
        jobs = Job.objects.all()
        serializer = GetJobsSerializer(jobs, many=True)
        return Response(serializer.data, status=200)
    
class CheckUserProfile(APIView):
    def get(self, request, username, *args, **kwargs):
        profile = UserProfile.objects.filter(user__username = username).first()
        if profile and profile.resume != None:
            return Response({'Msg': 'Found'}, status=200)
        return Response({'Not found'}, status=404)
    
class ApplyJob(APIView):
    def post(self, request, *args, **kwargs):
        serializer = JobApplicatonSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class UserProfileView(APIView):
    def get(self, request, username, *args, **kwargs):
        profile = UserProfile.objects.filter(user__username = username).first()
        if not profile:
            return Response({'Msg': 'Profile not found'}, status=404)
        return Response(ProfileUpdateSerializer(profile).data, status=200)
    
    def put(self, request, username, *args, **kwargs):
        profile = UserProfile.objects.filter(user__username = username).first()
        if not profile:
            return Response({'Msg': 'Profile not found'}, status=404)
        serializer = ProfileUpdateSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    



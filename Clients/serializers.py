from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'user', 'logo', 'web', 'email', 'description']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'company', 'salary', 'description', 'skills', 'education', 'experience', 'location', 'type']

class GetJobsSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Job
        fields = ['id','title', 'company', 'salary', 'description', 'skills', 'education', 'experience', 'location', 'type', 'post_date', 'deadline']

class JobApplicatonSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields =['id', 'job', 'user']

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['name', 'phone', 'resume']

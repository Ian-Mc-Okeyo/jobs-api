from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    resume = models.FileField(upload_to='resume', null=True, blank=True)

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='logos', null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    web = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)

job_types = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Freelance', 'Freelance'),
    ('Remote', 'Remote'),
)
experience = (
    ('1-2', '1-2'),
    ('2-3', '2-3'),
    ('3-6', '3-6'),
    ('6 or more', '6 or more'),
)

class Job(models.Model):
    title = models.CharField(max_length=200, default='Job')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    post_date = models.DateField(auto_now=True)
    location = models.CharField(max_length=200)
    salary  = models.CharField(max_length=200, null=True, blank=True)
    deadline = models.DateField(null=True)
    description = models.TextField(null=True)
    experience = models.CharField(max_length=200, choices=experience)
    education = models.TextField(null=True)
    skills = models.TextField(null=True)
    type = models.CharField(max_length=200, choices=job_types)

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

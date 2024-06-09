from django.urls import path
from .views import *


urlpatterns = [
    path('client-register/', RegisterClient.as_view(), name='register-client'),
    path('client-login/', ClientLogin.as_view(), name='client-login'),
    path('company-create/', ComapnyCreateUpdateView.as_view(), name='company-create'),
    path('job-create/<int:id>/', PostJob.as_view(), name='job-create'),
    path('get-jobs/', GetJobs.as_view(), name='jobs-all'),
    path('check-profile/<str:username>/', CheckUserProfile.as_view(), name='check-user-profile'),
    path('apply-job/', ApplyJob.as_view(), name='apply-job'),
    path('user-profile/<str:username>/', UserProfileView.as_view(), name='user-profile'),
]
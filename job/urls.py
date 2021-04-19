from django.contrib import admin
from django.urls import path , include

from . import views
app_name='job'

urlpatterns = [
    path('',views.job_list,name='job_list' ),
    path('add',views.add_job, name='add_job' ),
   # path('<int:id>',views.job_details, name='job_detail' ),
   path('<str:slug>',views.job_details, name='job_detail' ),
   
]
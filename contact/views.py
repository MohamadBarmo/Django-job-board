from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def send_message(request):
    myinfo=Info.objects.last()
    if request.method=="POST":
        subject=request.POST['subject']
        mail=request.POST['email']
        message=request.POST['message']
        name=request.POST['name']
        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [mail],
        
)
    
    return render(request,'contact/contact.html',{'myinfo':myinfo})




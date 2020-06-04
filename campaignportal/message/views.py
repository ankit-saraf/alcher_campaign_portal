from django.shortcuts import render
from .models import *
from django.utils import timezone


# Create your views here.
def home(request):
    allmessages=Message.objects.filter(admin_approved=True).order_by('-pub_date')
    socialmessages=socialMessage.objects.filter(admin_approved=True)
    return render(request, 'message/home.html',{'allmessages':allmessages , 'socialmessages' : socialmessages})

def submit(request):
    if request.method=='POST':
        if request.POST['message']:
            message1=Message()
            message1.message= request.POST['message']
            message1.pub_date= timezone.datetime.now()
            message1.save()
            allmessages=Message.objects.filter(admin_approved=True)
            socialmessages=socialMessage.objects.filter(admin_approved=True)
            return render(request, 'message/home.html', {'error':'Your message has been submitted successfully. You can see it in  recent message once it get approved.','allmessages':allmessages ,'socialmessages' : socialmessages})
        else:
            allmessages=Message.objects.filter(admin_approved=True)
            socialmessages=socialMessage.objects.filter(admin_approved=True)
            return render(request, 'message/home.html', {'error':'Please type the message.','allmessages':allmessages ,'socialmessages' : socialmessages })

    else:
        allmessages=Message.objects.filter(admin_approved=True)
        socialmessages=socialMessage.objects.filter(admin_approved=True)
        return render(request, 'message/home.html',{'allmessages':allmessages, 'socialmessages' : socialmessages})

def view_messages(request):
    allmessages=Message.objects.filter(admin_approved=True)
    socialmessages=socialMessage.objects.filter(admin_approved=True)
    return render(request, 'message/home.html',{'allmessages':allmessages , 'socialmessages' : socialmessages})

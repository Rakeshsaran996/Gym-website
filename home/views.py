from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def services(request):
   return render(request,'services.html')
def contact(request):
    if request.method =="POST":
        First_name = request.POST.get('First_name')
        Last_name = request.POST.get('Last_name')
        phone_no = request.POST.get('phone_no')
        City = request.POST.get('City')
        state = request.POST.get('state')
        Zip = request.POST.get('Zip')
        contact = Contact(First_name=First_name, Last_name=Last_name, phone_no=phone_no ,City=City ,state=state, Zip=Zip)
        contact.save()
    return render(request,'contact.html')

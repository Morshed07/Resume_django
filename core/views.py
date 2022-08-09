from django.shortcuts import render , HttpResponse
from datetime import datetime
from core.models import Contact
# Create your views here.
def home(request):
    context ={'home':'active'}
    return render(request,'core/home.html',context)
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        
        contact = Contact(name=name,email=email,msg=msg,date=datetime.today())
        contact.save()
    context ={'contact':'active'}
    return render(request,'core/contact.html',context)
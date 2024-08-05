from django.shortcuts import render, HttpResponse
from datetime import datetime
from MyApp.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
  context = {
    'variable' : "variable is sent"
  }
  messages.success(request, "Programming test")
  return render(request, "index.html", context)
  # return HttpResponse("This is the home page of MyApp")
  
def about(request):
  return render(request, "about.html")
  
def services(request):
  return render(request, "products.html")
  
def contacts(request):
  if request.method == "POST":
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    desc = request.POST.get('desc')
    contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
    contact.save()
    messages.success(request, "Successfully Submitted.Thanks for contacting us!")


  return render(request, "contacts.html")
 

from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.


def home(request):
  
  
  return render(request,'home.html')

def about(request):
  return render(request,'about.html')
  
def contact_us(request):
  return render(request,'Contact.html')

def perfume(request):
  Aroma=Perfume.objects.all()
  
  data={
    
    'Aroma': Aroma,
  }
  
  return render(request,'Perfume.html')
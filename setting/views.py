from django.views.generic.list import ListView

from django.shortcuts import render
from .models import imagelist, section_four, section_three, subservice

# Create your views here.





def home(request):
    image = imagelist.objects.all()
    
    service = subservice.objects.all()
    sethree =section_three.objects.all()
    sefour =section_four.objects.all()
   
    return render(request,"index.html",{
        "image":image,
        
        "service":service,
        "three":sethree,
       " four":sefour,
       

    })


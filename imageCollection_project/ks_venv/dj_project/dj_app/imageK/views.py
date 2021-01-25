from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    cats=Category.objects.all()
    images=Image.objects.order_by('-added_date')

    #search 
    search_term=''
    if 'search' in request.GET:
        search_term = request.GET['search']
        images=Image.objects.filter(title__icontains=search_term).order_by('-added_date')

    data={'images':images,'cats':cats}
    return render(request,'imageK/home.html',data)

def category(request, cid):
    catgories=Category.objects.all()

    cat=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=cat)

    data={'images':images,'cats':catgories}
    return render(request,'imageK/home.html',data)   

def sfs(request):
    return render(request,'imageK/sfs.html')  

    

    
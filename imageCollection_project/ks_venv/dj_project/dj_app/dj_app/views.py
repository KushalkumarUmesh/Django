from django.shortcuts import render

def show_about_page(request):
    return render(request,'about.html')
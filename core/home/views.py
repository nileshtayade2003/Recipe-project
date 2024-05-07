from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request,'index.html',context={'title':'home page'})

def contact(request):
    return render(request,"contact.html",context={'title':'contact us'})

def success_page(request):
    print("*"*10) #logic
    return HttpResponse("<h1>This is Success page.</h1>")

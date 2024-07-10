from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #return HttpResponse("Hello World... ")
    return render(request,'index.html')



def blog(request):
    return HttpResponse("blog... ")



def about(request):
    return HttpResponse("about .... ")
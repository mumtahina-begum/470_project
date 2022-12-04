from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("this is homepage")
    return render(request, 'templates/index.html')

def about (request):
    return HttpResponse("this is about page")   

def service (request):
    return HttpResponse("this is services page") 

def contact (request):
    return HttpResponse("contact us here")          


from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(req):
	return HttpResponse("<h1>Welocme</h1>")
def home(req):
	return HttpResponse("<h1>hello</h1>")
def index(req,name,roll):
	return HttpResponse("Hello " + name + " your roll number: " + str(roll))
def about(req):
	return render(req,'about.html')
def register(req):
	return render(req,'Student/register.html')
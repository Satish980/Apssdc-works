from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(req):
	return render(req, "index.html")

def home(req):
	return render(req, "home.html")

def resume(req):
	return render(req, "resume.html")

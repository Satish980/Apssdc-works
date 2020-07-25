from django.shortcuts import render
from Action.models import *
from django.http import HttpResponse

# Create your views here.
def index(req):
	return render(req,'includes/index.html')
def home(req):
	return render(req,'Action/home.html')
def about(req):
	return render(req,"Action/about.html")
def register(req):
	if req.method == "POST":
		name = req.POST['hname']
		age = req.POST['age']
		email = req.POST['email']
		password = req.POST['password']
		mname = req.POST['mname']

		data = Heroin_register(h_name = name,
							   h_age = age,
							   h_email = email,
							   h_password = password,
							   h_manager_name = mname
							   )
		data.save()
		return HttpResponse("Data Added Successfully")
	return render(req,"Action/register.html")
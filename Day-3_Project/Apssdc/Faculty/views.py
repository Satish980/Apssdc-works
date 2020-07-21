from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def showdata(req):
	info = {
			"name":"Satish",
			"Roll":"980",
			"age":"20"
	}
	return render(req,'templates/Faculty/showdata.html',{'info':info})

def fregister(req):
	if req.method == "POST":
		name = req.POST['name']
		email = req.POST['email']
		f_id = req.POST['id']
		age = req.POST['age']

		return HttpResponse("Hi Mr."+name+"\n"+"Email: "+email+"\n"+"ID: "+f_id+"\n"+"Age: "+age)
		#return render(req, 'Faculty/success.html',{'email':email})




	return render(req, 'Faculty/fregistration.html')
from django.shortcuts import render
#from . import views
from django.http import HttpResponse
from .models import StudentRegister,FacultyRegister
from .forms import StudentRegisterForm,FacultyRegisterForm
from django.core.mail import EmailMessage
from course import settings

# Create your views here.

def student_register(req):
	form = StudentRegisterForm(req.POST)
	if req.method == 'POST':
		if form.is_valid():
			student = StudentRegister(name = req.POST.get('name'),
									  email = req.POST.get('email'),
									  phone = req.POST.get('phone'),
									  age = req.POST.get('age'),
									  gender = req.POST.get('age'),
									  dob = req.POST.get('dob'))
			student.save()
			#name = req.POST.get('name')
			name = form.data['name']
			receiver = form.data['email']
			sub = 'Course Registration'
			body = 'hi '+name+" Your course registration has been done "\
					" successfully!!"
			sender = settings.EMAIL_HOST_USER

			email_msg = EmailMessage(sub, body, sender, [receiver])
			email_msg.send()
			return HttpResponse("Student registration completed")
	return render(req,'user/student_register.html',{'form':form})


def faculty_register(req):
	form = FacultyRegisterForm(req.POST)
	if req.method == 'POST':
		if form.is_valid():
			form.save()
			return HttpResponse("Faculty registration completed")
	return render(req,"user/faculty_register.html",{'form':form})


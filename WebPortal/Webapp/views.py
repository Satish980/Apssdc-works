from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMessage
from WebPortal import settings
# Create your views here.

def home(req):
	return render(req,'home.html')


def signup(req):
	form = UserForm()
	if(req.method == 'POST'):
		form = UserForm(req.POST)
		if(form.is_valid()):
			form.save()
			name = form.data['first_name'] + form.data['last_name']
			receiver = form.data['email']
			sub = 'Registration Successfull'
			body = "Hi, "+ name + "\n" + "Thanks For Registring to our Web Portal "\
			       "You can change your password anytime"
			sender = settings.EMAIL_HOST_USER

			email_msg = EmailMessage(sub, body, sender, [receiver])
			email_msg.send()
		return redirect('signin')

	return render(req, 'register.html',{'form':form})

def signin(req):
	if(req.method == "POST"):
		username = req.POST['username']
		password = req.POST['password']
		user = authenticate(username=username,password=password)
		if(user is not None):
			messages.info(req,'Successfully Login')
			login(req,user)
		else:
			messages.error(req,"Invalid Credentials")
			#return render(req,'home.html')
			return redirect('signin')
	#messages.warning(req,"Invalid Credentials")
	return render(req, 'home.html')

@login_required
def signout(req):
	logout(req)
	return redirect('home')

@login_required
def profile(req):
	messages.info(req,'Successfully Login')
	user = get_user(req)
	return render(req,'profile.html',{'user':user})

#for password changing
@login_required
def changepassword(req):
	form = PasswordChangeForm(req.user)
	if(req.method == 'POST'):
		form = PasswordChangeForm(req.user,req.POST)
		if(form.is_valid()):
			update = form.save()
			update_session_auth_hash(req,update)
			return redirect('login.html')
	return render(req,'changepassword.html',{'form':form})

def changesuccess(req):
	logout(req)
	return render(req,'login.html')

def showusers(req):
	data = User.objects.all()
	return render(req,'showusers.html',{'data':data})

def edituser(req,id):
	user = User.objects.get(id = id)
	if req.method == 'POST':
		first_name = req.POST['first_name']
		last_name = req.POST['last_name']
		username = req.POST['username']
		email = req.POST['email']
		user.first_name = first_name
		user.last_name = last_name
		user.username = username
		user.email = email
		user.save()
		messages.info(req,'%s is Successfully Updated'%(username))
		return redirect('showusers')
	return render(req,'edituser.html',{'user':user})

def deleteuser(req,id):
	user = User.objects.get(id = id)
	if req.method == 'POST':
		user.delete()
		messages.error(req,'Successfully deleted')
		return redirect('showusers')
	return render(req, 'deleteuser.html',{'user':user})

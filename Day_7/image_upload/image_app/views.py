from django.shortcuts import render
from django.http import HttpResponse
from .models import Upload
from .forms import UploadForm
# Create your views here.
def display(req):
	return HttpResponse("For image display",{'data':form})
	

def index(req):
	form = UploadForm(req.POST,req.FILES)
	if form.is_valid():
		form.save()
		return HttpResponse('done!')

	return render(req,'index.html',{'data':form} )

	

	

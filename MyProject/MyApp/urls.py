from django.urls import path
from MyApp import views

urlpatterns = [
			
			path('index/',views.index,name = "index"),
			path('home/',views.home,name = "home"),
			path('resume/',views.resume,name = "resume"),	
]
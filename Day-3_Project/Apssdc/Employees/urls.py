from django.urls import path
from Employees import views

urlpatterns = [
    path('apssdc/', views.home,name = "home"),
    path('index/<str:name>/<int:roll>',views.index,name = "index"),
    path('about/',views.about,name = "about"),
    path('register',views.register,name = "register")
    
]
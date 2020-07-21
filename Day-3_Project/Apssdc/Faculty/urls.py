from django.urls import path,include
from Faculty import views

urlpatterns = [
    path('showdata/', views.showdata,name = "showdata"),
    path('Register/',views.fregister,name = "fregister"),
]
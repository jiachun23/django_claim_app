from django.urls import path
from . import views


app_name = 'claims'

urlpatterns = [
    
    path('view/', views.viewlist , name="viewlist"),
    path('index/', views.index, name="index"),
    path('index/add/', views.add_record, name="add_record"),
 
]


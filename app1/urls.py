from django.urls import path
from app1 import views

app_name = 'app1'

urlpatterns = [ 

    path('students',views.students,name='students'),
    path('sonu',views.sonu,name='sonu'),
]
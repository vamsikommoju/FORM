from django.shortcuts import render
from app1.forms import Personsform
from app1.models import Persons

# Create your views here.

def index(request):
    return render(request,'app1/index.html',{'msg':'This is Index Page'})


def students(request):
    data = ['tabusha','vamsi','srinu','kiran','teja','raju']
    context = {'data':data}
    return render(request,'app1/student.html',context)
    
def sonu(request):
    form = Personsform()
    if request.method == 'POST':
        form = Personsform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            gender=form.cleaned_data['gender']
            phno=form.cleaned_data['phno']
            A = Persons(name=name,age=age,gender=gender,phno=phno)
            A.save()
            form = Personsform()    
        else:
            print('notvalid')
    context = {'msg':'this is students page','form':form}
    return render(request,'app1/sonu.html',context)
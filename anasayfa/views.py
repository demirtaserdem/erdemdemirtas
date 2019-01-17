from django.shortcuts import render,HttpResponse,redirect
from .models import Person
from .forms import PersonForm

# Create your views here.

def index(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("anasayfa:index")

    persons = Person.objects.all()
    context = {
        "elma":persons,
        "form":form
    } 
    return render(request,"index.html",context)

    


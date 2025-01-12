from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Ring
from django.views.generic import CreateView,DeleteView,UpdateView
from .forms import PolishingForm

# Create your views here.

class RingCreate(CreateView):
    model=Ring
    fields=['name','size','description','price','image']

class RingUpdate(UpdateView):
    model=Ring
    fields=['name','size','price']
    
class RingDelete(DeleteView):
    model=Ring
    success_url='/rings/'

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def ring_index(request):
    #This will Select from main_app (Select * from main_app)
    rings = Ring.objects.all()
    return render(request, 'rings/index.html',{'rings':rings})
def rings(request,ring_id):
    ring = Ring.objects.get(id=ring_id)
    polishing_form=PolishingForm()
    return render(request,'rings/detail.html',{'ring':ring,'polishing_form':polishing_form})

def add_polishing(request,ring_id):
    form =PolishingForm(request.POST)
    if form.is_valid():
        new_polishing=form.save(commit=False)
        new_polishing.ring_id=ring_id
        new_polishing.save()
    return redirect('detail',ring_id=ring_id)
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Ring,Band
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
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

class BandList(ListView):
    model=Band

class BandDetail(DetailView):
    model=Band

class BandCreate(CreateView):
    model=Band
    fields='__all__'

class BandUpdate(UpdateView):
    model=Band
    fields=['name','size']

class BandDelete(DeleteView):
    model=Band
    success_url='/bands/'

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
    
    bands_ring_doesnt_have=Band.objects.exclude(id__in=ring.bands.all().values_list('id'))

    
    return render(request,'rings/detail.html',{'ring':ring,'polishing_form':polishing_form,'bands':bands_ring_doesnt_have})

def add_polishing(request,ring_id):
    form =PolishingForm(request.POST)
    if form.is_valid():
        new_polishing=form.save(commit=False)
        new_polishing.ring_id=ring_id
        new_polishing.save()
    return redirect('detail',ring_id=ring_id)

def assoc_band(request,ring_id,band_id):
    Ring.objects.get(id=ring_id).bands.add(band_id)
    return redirect('detail',ring_id=ring_id)

def unassoc_band(request,ring_id,band_id):
    Ring.objects.get(id=ring_id).bands.remove(band_id)
    return redirect('detail',ring_id=ring_id)
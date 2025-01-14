from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Ring,Band
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .forms import PolishingForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class RingCreate(LoginRequiredMixin,CreateView):
    model=Ring
    fields=['name','size','description','price','image']
    def form_valid(self,form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class RingUpdate(LoginRequiredMixin,UpdateView):
    model=Ring
    fields=['name','size','price']
    
class RingDelete(LoginRequiredMixin,DeleteView):
    model=Ring
    success_url='/rings/'

class BandList(LoginRequiredMixin,ListView):
    model=Band

class BandDetail(LoginRequiredMixin,DetailView):
    model=Band

class BandCreate(LoginRequiredMixin,CreateView):
    model=Band
    fields='__all__'

class BandUpdate(LoginRequiredMixin,UpdateView):
    model=Band
    fields=['name','size']

class BandDelete(LoginRequiredMixin,DeleteView):
    model=Band
    success_url='/bands/'

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

@login_required
def ring_index(request):
    #This will Select from main_app (Select * from main_app)
    # rings = Ring.objects.all()
    rings=Ring.objects.filter(user=request.user)
    return render(request, 'rings/index.html',{'rings':rings})

@login_required
def rings(request,ring_id):
    ring = Ring.objects.get(id=ring_id)
    polishing_form=PolishingForm()
    
    bands_ring_doesnt_have=Band.objects.exclude(id__in=ring.bands.all().values_list('id'))

    
    return render(request,'rings/detail.html',{'ring':ring,'polishing_form':polishing_form,'bands':bands_ring_doesnt_have})

@login_required
def add_polishing(request,ring_id):
    form =PolishingForm(request.POST)
    if form.is_valid():
        new_polishing=form.save(commit=False)
        new_polishing.ring_id=ring_id
        new_polishing.save()
    return redirect('detail',ring_id=ring_id)

@login_required
def assoc_band(request,ring_id,band_id):
    Ring.objects.get(id=ring_id).bands.add(band_id)
    return redirect('detail',ring_id=ring_id)

@login_required
def unassoc_band(request,ring_id,band_id):
    Ring.objects.get(id=ring_id).bands.remove(band_id)
    return redirect('detail',ring_id=ring_id)

def signup(request):
    error_message=''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)#to login the user directly after signing up
            return redirect('index')
        else:
            error_message='Invalid Sign-up please try again later.'
    form = UserCreationForm()
    context={'form':form,'error_message':error_message}
    return render(request,'registration/signup.html',context)
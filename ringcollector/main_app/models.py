from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
POLISH=(
    ('S','Soft Cloth'),
    ('U','Ultrasonic Cleaner'),
    ('R','Rotary Tool')
)

class Band(models.Model):
    name=models.CharField(max_length=50)
    size=models.IntegerField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bands_detail',kwargs={'pk':self.id})

class Ring(models.Model):
    name=models.CharField(max_length=100)
    size=models.IntegerField()
    description=models.TextField(max_length=400)
    price=models.FloatField()
    image=models.ImageField(upload_to='main_app/static/uploads',default="")
    bands=models.ManyToManyField(Band)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'ring_id':self.id})
    def __str__(self):
        return self.name
    def pol_for_today(self):
        return self.polishing_set.filter(date=date.today()).count() >= 1

class Polishing(models.Model): 
    date=models.DateField()
    polish=models.CharField(max_length=1,choices=POLISH,default=POLISH[0][0])
    ring=models.ForeignKey(Ring,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.get_polish_display()} on {self.date} for {self.ring.name}'
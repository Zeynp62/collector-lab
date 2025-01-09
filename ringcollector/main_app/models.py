from django.db import models

# Create your models here.
class Ring(models.Model):
    name=models.CharField(max_length=100)
    size=models.IntegerField()
    description=models.TextField(max_length=250)
    price=models.FloatField()
    image=models.ImageField(upload_to='main_app/static/uploads',default="")
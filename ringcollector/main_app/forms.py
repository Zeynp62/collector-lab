from django.forms import ModelForm
from .models import Polishing

class PolishingForm(ModelForm):
    class Meta:
        model = Polishing 
        fields = ['date','polish']
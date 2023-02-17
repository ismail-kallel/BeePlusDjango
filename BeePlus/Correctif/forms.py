from django.forms import ModelForm
from . models import Avis

class AvisForm(ModelForm):
    class Meta:
        model = Avis
        fields = '__all__'
        
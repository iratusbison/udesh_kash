from django import forms
from .models import Supply 

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ['resource','quantity_supplied']
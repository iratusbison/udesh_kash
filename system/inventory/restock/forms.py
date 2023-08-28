from django import forms

from resource.models import Product
from .models import Restock

class SupplyForm(forms.ModelForm):
    class Meta:
        model = Restock
        fields = ['resource','quantity_refilled']

        
'''
    def __init__ (self, *args,**kwargs):
        super(SupplyForm, self).__init__(*args, **kwargs)
        self.fields['resource'].queryset = Product.object.all()
'''
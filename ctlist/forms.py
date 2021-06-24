from django import forms  
from .models import Bagahe  
    
class DeleteName(forms.ModelForm):  
    class Meta:  
        model = Bagahe  
        fields = "__all__"
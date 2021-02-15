from django import forms
from classbasedAPP.models import GeekModel

class GeekForm(forms.ModelForm):
    
    class Meta:
        model = GeekModel
        fields = [
            "title",
            "description",
        ]
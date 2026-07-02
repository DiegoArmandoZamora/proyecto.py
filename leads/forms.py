from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['nombre', 'telefono', 'email', 'direccion', 'telefono_alternativo', 'mensaje', 'imagen']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}),
            'mensaje': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Describe el daño en el techo...'}),
            'imagen': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
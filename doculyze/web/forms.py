from django import forms
from .models import Document
from django.forms import formset_factory

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file', )

class DocumentTempForm(forms.Form):
    name = forms.CharField(
        label='Doc-ID',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Filename', 
            'readonly' : 'readonly',            
        })
    )
DocumentTempFormset = formset_factory(DocumentTempForm, extra=1)
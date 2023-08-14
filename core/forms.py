from django import forms
from .models import (
    Document,
    Institution,
    InstitutionType,
    Category,
    DocumentType
)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'title',
            'institution',
            'category',
            'type',
            'year',
            'publisher',
            'note',
            'url'
        ]
        widgets = {
            'title': forms.Textarea(
                attrs={'rows': 1, 'required': True}
            ),
            'institution': forms.Select(
                attrs={'required': True}
            ),
            'category': forms.Select(
                attrs={'required': True}
            ),
            'type': forms.Select(
                attrs={'required': True}
            ),
            'year': forms.NumberInput(
                attrs={'placeholder': 'YYYY', 'min': 1900, 'max': 3000}
            ),
            'publisher': forms.Textarea(
                attrs={'rows': 1,}
            ),
            'note': forms.Textarea(
                attrs={'rows': 3}
            ),
            'url': forms.Textarea(
                attrs={'rows': 1, 'required': True}
            ),
        }
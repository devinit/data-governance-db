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

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['institution'].queryset = self.fields['institution'].queryset.order_by('name')
        self.fields['category'].queryset = self.fields['category'].queryset.order_by('name')
        self.fields['type'].queryset = self.fields['type'].queryset.order_by('name')


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = [
            'name',
            'type'
        ]
        widgets = {
            'name': forms.Textarea(
                attrs={'rows': 1, 'required': True}
            ),
            'type': forms.Select(
                attrs={'required': True}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(InstitutionForm, self).__init__(*args, **kwargs)
        self.fields['type'].queryset = self.fields['type'].queryset.order_by('name')


class InstitutionTypeForm(forms.ModelForm):
    class Meta:
        model = InstitutionType
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.Textarea(
                attrs={'rows': 1, 'required': True}
            ),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.Textarea(
                attrs={'rows': 1, 'required': True}
            ),
        }


class DocumentTypeForm(forms.ModelForm):
    class Meta:
        model = DocumentType
        fields = [
            'name',
        ]
        widgets = {
            'name': forms.Textarea(
                attrs={'rows': 1, 'required': True}
            ),
        }
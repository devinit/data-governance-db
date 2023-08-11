from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

    def clean_email(self):
        data = self.cleaned_data['email']
        domain = data.split('@')[1]
        domain_list = ["devinit.org",]
        if domain not in domain_list:
            raise forms.ValidationError("Please enter a valid Development Initiatives email address.")
        return data

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

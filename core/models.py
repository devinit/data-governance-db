from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from ckeditor.fields import RichTextField


def validate_url(value):
    na_variations = [
        "n.a.",
        "na",
        "na."
        "n.a"
    ]
    if not str(value).lower() in na_variations:
        validator = URLValidator()
        validator(value)


class Document(models.Model):
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:document_detail', kwargs={'id': self.id})

    institution = models.ForeignKey(
        'Institution',
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'documents'
    )

    category = models.ForeignKey(
        'Category',
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'documents'
    )

    type = models.ForeignKey(
        'DocumentType',
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = 'documents'
    )

    title = models.TextField()

    year = models.IntegerField(
        blank = True,
        null = True
    )

    publisher = models.TextField(
        blank = True,
        null = True
    )

    note = models.TextField(
        blank = True,
        null = True
    )

    url = models.TextField(
        blank = True,
        null = True,
        help_text='Enter either a valid URL, or "n.a." if not available.',
        validators = [validate_url]
    )


class Institution(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:institution_detail', kwargs={'id': self.id})

    name = models.TextField()

    type = models.ForeignKey(
        'InstitutionType',
        blank = True,
        null = True,
        on_delete = models.SET_NULL,
        related_name = "institutions"
    )


class InstitutionType(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:institution_type_detail', kwargs={'id': self.id})

    name = models.TextField()


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:category_detail', kwargs={'id': self.id})

    name = models.TextField()


class DocumentType(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:document_type_detail', kwargs={'id': self.id})

    name = models.TextField()


class HomePageSettings(models.Model):
    class Meta:
        verbose_name_plural = 'home page settings'

    def __str__(self):
        return "Home page settings"

    def clean(self):
        if HomePageSettings.objects.exists() and not self.pk:
            raise ValidationError("You can only have one home page settings object.")

    authenticated_content = RichTextField(help_text="Home page content that will appear to logged-in users.")
    unauthenticated_content = RichTextField(help_text="Home page content that will appear to new users above the register/login links.")

from django.db import models
from django.urls import reverse


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

    url = models.URLField(
        max_length = 9999,
        blank = True,
        null = True
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
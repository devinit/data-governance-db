# Generated by Django 4.2.4 on 2023-08-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_document_abstract'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='full_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]

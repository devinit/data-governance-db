# Generated by Django 4.2.4 on 2023-08-11 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institutions', to='core.institutiontype'),
        ),
    ]

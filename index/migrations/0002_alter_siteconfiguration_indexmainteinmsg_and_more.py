# Generated by Django 4.0.2 on 2022-02-02 23:52

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='indexMainteinMsg',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='indexPageMsg',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]

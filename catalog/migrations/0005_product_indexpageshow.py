# Generated by Django 4.0.2 on 2022-02-02 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_remove_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='indexPageShow',
            field=models.BooleanField(default=False, verbose_name='indexPageShow'),
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-02 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_product_images_delete_productimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-02 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.image')),
                ('subCategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.subcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.image')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
        migrations.CreateModel(
            name='Category_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('imageId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.image')),
            ],
        ),
    ]

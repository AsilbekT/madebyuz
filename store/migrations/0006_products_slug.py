# Generated by Django 4.0.3 on 2022-03-30 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_products_picture_for_mini_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]

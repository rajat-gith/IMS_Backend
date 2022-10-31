# Generated by Django 4.1.1 on 2022-10-08 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0012_remove_stores_brands_brand_corresponding_stores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='corresponding_stores',
        ),
        migrations.AddField(
            model_name='stores',
            name='brands',
            field=models.ManyToManyField(to='src.brand'),
        ),
    ]

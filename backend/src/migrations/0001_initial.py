# Generated by Django 4.1.1 on 2022-11-08 03:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('A', 'Active'), ('B', 'Inactive')], max_length=200, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='store_owner',
            fields=[
                ('owner_name', models.CharField(blank=True, max_length=200, null=True)),
                ('store_count', models.IntegerField(blank=True)),
                ('sex', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('owner_status', models.CharField(blank=True, choices=[('A', 'Active'), ('B', 'Inactive')], max_length=200, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='stores',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('tagline', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('A', 'Active'), ('B', 'Inactive')], max_length=200, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('brands', models.ManyToManyField(to='src.brand')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='src.store_owner')),
            ],
        ),
        migrations.CreateModel(
            name='sales',
            fields=[
                ('date_of_dispatch', models.DateTimeField(blank=True, null=True)),
                ('quantity_shipment', models.IntegerField(blank=True, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('depart_store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Departed_Store', to='src.stores')),
                ('destination_store', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Destination_Store', to='src.stores')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('color', models.CharField(blank=True, choices=[('Blue', 'Blue'), ('Black', 'Black'), ('Red', 'Red'), ('White', 'White'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('Purple', 'purple')], max_length=200)),
                ('category', models.CharField(blank=True, choices=[('Men', 'Men'), ('Women', 'Women'), ('Child', 'Child'), ('Unisex', 'Unisex')], max_length=200)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='src.brand')),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-16 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('purchaseOrderId', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=100)),
                ('pricing', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('mrp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('customerId', models.AutoField(primary_key=True, serialize=False)),
                ('customerName', models.CharField(max_length=100)),
                ('mobileNumber', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('shippingId', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('purchaseOrderId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task_apis.orders')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='customerId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Task_apis.users'),
        ),
    ]
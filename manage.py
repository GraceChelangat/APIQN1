# 0001_initial.py
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Account Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Order Date')),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('CANCELED', 'Canceled')], default='PENDING', max_length=20, verbose_name='Order Status')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_name.customer', verbose_name='Customer')),
            ],
        ),
    ]

# 0001_initial.py
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        # Creating the Customer model
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Primary key for Customer
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),  # Customer's first name
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),  # Customer's last name
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),  # Unique email for each customer
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),  # Optional phone number
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),  # Optional address
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Account Created At')),  # Timestamp for account creation
            ],
        ),
        # Creating the Order model
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # Primary key for Order
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='Order Date')),  # Auto-generated order date
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('SHIPPED', 'Shipped'), ('DELIVERED', 'Delivered'), ('CANCELED', 'Canceled')], default='PENDING', max_length=20, verbose_name='Order Status')),  # Order status with predefined choices
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Amount')),  # Decimal field for order total
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_name.customer', verbose_name='Customer')),  # One-to-many relationship with Customer
            ],
        ),
    ]

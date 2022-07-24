# Generated by Django 3.1.7 on 2021-09-05 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_customer_paid_until'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer_membership', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20210413_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cancel_at_period_end',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='membership',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='paid_until',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='stripeid',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='stripesubscription',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

# Generated by Django 3.1.4 on 2021-01-12 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(default=None, editable=False, max_length=100),
        ),
    ]

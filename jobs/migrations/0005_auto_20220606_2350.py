# Generated by Django 3.1.7 on 2022-06-06 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20211118_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]

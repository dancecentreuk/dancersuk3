# Generated by Django 3.1.7 on 2021-04-05 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20210405_1258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dancestyle',
            old_name='title',
            new_name='name',
        ),
    ]

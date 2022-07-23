# Generated by Django 3.1.4 on 2021-02-18 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_dancersprofile_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='DancerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/dancers_image_collection/%Y/%m/%d')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.dancersprofile')),
            ],
        ),
    ]

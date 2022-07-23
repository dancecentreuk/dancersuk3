# Generated by Django 3.1.4 on 2021-01-12 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(default=None, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('location', models.CharField(choices=[('brighton', 'Brighton'), ('leeds', 'Leeds'), ('liverpool', 'Liverpool'), ('manchester', 'Manchester'), ('nottingham', 'Nottingham'), ('portsmouth', 'Portsmouth'), ('reading', 'Reading')], default=None, max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('start_time', models.CharField(blank=True, max_length=10, null=True)),
                ('end_time', models.CharField(blank=True, max_length=10, null=True)),
                ('rehearsal_date', models.CharField(blank=True, max_length=250)),
                ('fee', models.CharField(max_length=200)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('is_posting', models.BooleanField(default=True)),
                ('is_published', models.BooleanField(default=True)),
                ('is_allowed', models.BooleanField(default=True)),
                ('listing_image', models.ImageField(default='dance_class.jpg', upload_to='listing_image/%Y/%m/%d')),
                ('slug', models.SlugField(default=None, editable=False)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='jobs.category')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

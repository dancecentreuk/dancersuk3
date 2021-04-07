# Generated by Django 3.1.4 on 2021-03-11 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
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
        migrations.AlterField(
            model_name='blogpost',
            name='is_allowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.category'),
        ),
    ]

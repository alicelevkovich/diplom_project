# Generated by Django 3.1.4 on 2020-12-22 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_blog', '0009_auto_20201222_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
# Generated by Django 3.1.4 on 2020-12-22 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_blog', '0007_auto_20201222_1203'),
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

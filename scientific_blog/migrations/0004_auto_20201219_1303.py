# Generated by Django 3.1.4 on 2020-12-19 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scientific_blog', '0003_auto_20201219_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lab', to='scientific_blog.lab'),
        ),
    ]

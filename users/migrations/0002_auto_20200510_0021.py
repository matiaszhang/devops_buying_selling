# Generated by Django 2.2.10 on 2020-05-09 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(model_name='profile', name='image', field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),),
    ]

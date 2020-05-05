# Generated by Django 2.2.10 on 2020-05-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200504_2224'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='post',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='post',
            field=models.ManyToManyField(to='posts.Post'),
        ),
    ]
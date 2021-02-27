# Generated by Django 3.0.8 on 2021-02-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0010_pickedimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pickedimage',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='pickedimage',
            name='cover_image',
            field=models.ManyToManyField(to='Gallery.ImagesClient'),
        ),
    ]
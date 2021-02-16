# Generated by Django 3.0.8 on 2021-01-16 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0004_auto_20210115_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlatformPresentationImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='gallery_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='imagesclient',
            name='image',
            field=models.ImageField(upload_to='gallery_images/'),
        ),
    ]

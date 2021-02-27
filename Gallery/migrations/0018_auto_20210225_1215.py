# Generated by Django 3.0.8 on 2021-02-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0017_auto_20210225_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesclient',
            name='pick_back_image',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AlterField(
            model_name='imagesclient',
            name='pick_content_image_four',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AlterField(
            model_name='imagesclient',
            name='pick_content_image_one',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AlterField(
            model_name='imagesclient',
            name='pick_content_image_three',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AlterField(
            model_name='imagesclient',
            name='pick_content_image_two',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
        migrations.AlterField(
            model_name='imagesclient',
            name='pick_cover_image',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], default='NO', max_length=5),
        ),
    ]
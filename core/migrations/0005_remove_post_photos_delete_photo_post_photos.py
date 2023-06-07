# Generated by Django 4.1.7 on 2023-06-04 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_photo_remove_post_photos_post_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photos',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='post',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
# Generated by Django 4.1.7 on 2023-06-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_post_photos_delete_photo_post_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photos1',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='photos2',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='photos3',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='photos4',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
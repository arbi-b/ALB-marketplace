# Generated by Django 4.1.7 on 2023-07-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]

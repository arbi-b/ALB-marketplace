# Generated by Django 4.1.7 on 2023-07-16 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
    ]

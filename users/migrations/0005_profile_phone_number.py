# Generated by Django 4.1.7 on 2023-07-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(default='0', max_length=20),
        ),
    ]

# Generated by Django 4.1.7 on 2023-07-11 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=10),
        ),
    ]

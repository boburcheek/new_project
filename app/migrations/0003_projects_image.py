# Generated by Django 4.2.1 on 2023-06-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_service_image_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
    ]
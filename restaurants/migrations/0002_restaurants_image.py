# Generated by Django 4.2.4 on 2023-08-15 15:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='logos'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='/Drf-api/default_profile_ubr0la', upload_to='images'),
        ),
    ]
# Generated by Django 5.0.6 on 2024-11-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
    ]
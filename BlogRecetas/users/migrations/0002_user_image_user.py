# Generated by Django 4.0.4 on 2022-07-04 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image_user',
            field=models.ImageField(blank=True, null=True, upload_to='users'),
        ),
    ]
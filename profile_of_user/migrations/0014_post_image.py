# Generated by Django 3.1.7 on 2021-06-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_of_user', '0013_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]

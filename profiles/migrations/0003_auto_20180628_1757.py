# Generated by Django 2.0.6 on 2018-06-28 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_profileimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profileImage',
            new_name='profile_image',
        ),
    ]

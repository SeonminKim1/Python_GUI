# Generated by Django 4.0.4 on 2022-04-29 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='profle_image',
            new_name='profile_image',
        ),
    ]

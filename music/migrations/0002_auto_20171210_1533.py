# Generated by Django 2.0 on 2017-12-10 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_type',
            new_name='song_title',
        ),
    ]

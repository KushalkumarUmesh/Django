# Generated by Django 3.0.8 on 2020-07-29 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageK', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='title',
            new_name='location',
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-30 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageK', '0003_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(default=''),
        ),
    ]

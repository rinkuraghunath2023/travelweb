# Generated by Django 4.1.7 on 2023-03-07 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelwebapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Place',
            new_name='Places',
        ),
        migrations.RenameField(
            model_name='places',
            old_name='img',
            new_name='image',
        ),
    ]
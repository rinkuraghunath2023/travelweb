# Generated by Django 4.1.7 on 2023-03-07 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelwebapp', '0002_rename_place_places_rename_img_places_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Places',
            new_name='OurPlaces',
        ),
    ]

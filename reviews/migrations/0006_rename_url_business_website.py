# Generated by Django 5.0.2 on 2024-02-13 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_rename_contry_business_country'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='url',
            new_name='website',
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='business',
        ),
        migrations.AddField(
            model_name='category',
            name='business',
            field=models.ManyToManyField(to='reviews.business'),
        ),
    ]

# Generated by Django 5.0 on 2024-01-10 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('University', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='YOE',
            field=models.IntegerField(default=1992),
        ),
    ]

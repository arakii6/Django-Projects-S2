# Generated by Django 5.0 on 2024-01-14 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['Name'], 'verbose_name_plural': 'Customer'},
        ),
    ]
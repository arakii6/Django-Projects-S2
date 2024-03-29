# Generated by Django 5.0 on 2024-01-10 16:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Department',
                'ordering': ['department_name'],
            },
        ),
        migrations.CreateModel(
            name='StudentId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Student Id',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_age', models.PositiveBigIntegerField(default=18)),
                ('student_address', models.TextField(null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dept_std', to='University.department')),
                ('student_id', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stdid_std', to='University.studentid')),
            ],
            options={
                'verbose_name_plural': 'Student',
                'ordering': ['student_name'],
            },
        ),
    ]

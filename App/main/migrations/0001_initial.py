# Generated by Django 3.2.4 on 2023-11-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('timetable', models.TextField(verbose_name='timetable')),
                ('phone_number', models.CharField(max_length=100, verbose_name='phone_number')),
            ],
        ),
    ]
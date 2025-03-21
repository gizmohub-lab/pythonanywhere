# Generated by Django 5.1.6 on 2025-03-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('date', models.DateField(unique=True)),
                ('address', models.TextField()),
                ('program', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='homepagedesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]

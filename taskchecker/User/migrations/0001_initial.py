# Generated by Django 5.1.3 on 2024-11-06 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('role', models.CharField(max_length=255)),
                ('date_of_registration', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

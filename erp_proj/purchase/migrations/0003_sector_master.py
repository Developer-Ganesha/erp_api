# Generated by Django 5.0.6 on 2024-07-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_profile', models.CharField(max_length=200)),
                ('sector_name', models.CharField(max_length=200)),
            ],
        ),
    ]

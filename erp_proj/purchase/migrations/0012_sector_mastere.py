# Generated by Django 5.0.6 on 2024-07-29 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0011_item_parant_fg_code_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector_Mastere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_prefix', models.CharField(max_length=200)),
                ('sector_name', models.CharField(max_length=200)),
            ],
        ),
    ]

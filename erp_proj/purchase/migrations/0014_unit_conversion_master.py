# Generated by Django 5.0.6 on 2024-07-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0013_item_section_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_conversion_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_group', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('unit', models.CharField(max_length=200)),
                ('stock_qty', models.CharField(max_length=200)),
                ('stock_unit', models.CharField(max_length=200)),
            ],
        ),
    ]

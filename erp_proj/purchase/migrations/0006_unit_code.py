# Generated by Django 5.0.6 on 2024-07-27 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0005_business_partner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=200)),
                ('edit', models.CharField(max_length=200)),
                ('delete', models.CharField(max_length=200)),
            ],
        ),
    ]
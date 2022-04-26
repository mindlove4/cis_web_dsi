# Generated by Django 4.0.4 on 2022-04-17 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cisweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address_Student',
            fields=[
                ('address_stu_id', models.AutoField(primary_key=True, serialize=False)),
                ('house_number', models.CharField(max_length=255)),
                ('village_number', models.CharField(max_length=255)),
                ('soi', models.CharField(max_length=255)),
                ('road', models.CharField(max_length=255)),
                ('subdistrict', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('postcode', models.IntegerField(max_length=6, validators=[django.core.validators.MinLengthValidator(6)])),
            ],
        ),
    ]

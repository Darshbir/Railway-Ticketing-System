# Generated by Django 4.2.7 on 2024-01-19 07:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0018_alter_section_booked_seats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-26 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='destination',
            field=models.TextField(default='To be decided'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='name',
            field=models.CharField(default='Unknown', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='train',
            name='start',
            field=models.TextField(default='to be decided'),
            preserve_default=False,
        ),
    ]

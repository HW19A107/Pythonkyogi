# Generated by Django 4.1.3 on 2022-11-23 06:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kyogi', '0002_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='total',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

# Generated by Django 4.1.3 on 2022-11-24 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyogi', '0004_alter_total_clear_alter_total_clear_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='clear_time',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

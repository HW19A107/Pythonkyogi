# Generated by Django 4.1.3 on 2022-11-24 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kyogi', '0003_total_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='total',
            name='clear',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='total',
            name='clear_time',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='total',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='total',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='total',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]

# Generated by Django 2.0.4 on 2018-11-26 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20181126_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='closing_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='opening_time',
            field=models.TimeField(),
        ),
    ]

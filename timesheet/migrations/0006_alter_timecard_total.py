# Generated by Django 4.0.5 on 2022-07-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0005_alter_timecard_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]

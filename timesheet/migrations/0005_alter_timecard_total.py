# Generated by Django 4.0.5 on 2022-07-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0004_alter_timecard_clock_out_alter_timecard_lunch_in_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
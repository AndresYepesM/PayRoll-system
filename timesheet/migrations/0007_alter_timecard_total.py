# Generated by Django 4.0.5 on 2022-07-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet', '0006_alter_timecard_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timecard',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_employee_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='salary',
            field=models.FloatField(default=0.0),
        ),
    ]
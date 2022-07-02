# Generated by Django 4.0.5 on 2022-07-02 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_position_counter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='enterprise',
        ),
        migrations.AddField(
            model_name='position',
            name='enterprise',
            field=models.ManyToManyField(null=True, to='company.enterprise'),
        ),
    ]

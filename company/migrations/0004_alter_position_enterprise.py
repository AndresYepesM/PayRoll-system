# Generated by Django 4.0.5 on 2022-06-30 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_position_enterprise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='enterprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.enterprise'),
        ),
    ]

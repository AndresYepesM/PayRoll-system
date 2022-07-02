# Generated by Django 4.0.5 on 2022-07-02 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_alter_employee_role_alter_position_enterprise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.position'),
        ),
        migrations.AlterField(
            model_name='position',
            name='enterprise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.enterprise'),
        ),
    ]

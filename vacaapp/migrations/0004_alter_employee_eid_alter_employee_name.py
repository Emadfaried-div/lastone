# Generated by Django 4.1.7 on 2023-04-01 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacaapp', '0003_alter_employee_resdual_vacations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='eid',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 3.2.13 on 2023-04-11 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0003_auto_20230411_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkSchedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('lunch_break_start', models.TimeField()),
                ('lunch_break_end', models.TimeField()),
                ('created_by', models.CharField(max_length=255)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employees.employees')),
            ],
            options={
                'db_table': 'WorkSchedules',
            },
        ),
    ]

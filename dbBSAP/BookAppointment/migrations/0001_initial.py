# Generated by Django 4.2.8 on 2023-12-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dateOfAppointment', models.DateField()),
                ('timeOfAppointment', models.TimeField()),
                ('dateOfApproval', models.DateField()),
                ('appointmentStatus', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'Appointment',
            },
        ),
        migrations.CreateModel(
            name='HealthCenter',
            fields=[
                ('healthCenter_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('healthCenter_name', models.CharField(max_length=25)),
                ('contactInfo', models.CharField(max_length=11)),
            ],
            options={
                'db_table': 'HealthCenter',
            },
        ),
    ]

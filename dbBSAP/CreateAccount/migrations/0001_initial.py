# Generated by Django 4.2.8 on 2023-12-14 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BookAppointment', '0001_initial'),
        ('BorrowResource', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('R', 'Resident'), ('O', 'Organization'), ('A', 'Admin')], max_length=1)),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('birth_date', models.DateField()),
                ('present_address', models.CharField(max_length=50)),
                ('borrowed_resources', models.ManyToManyField(through='BorrowResource.BorrowResource', to='BorrowResource.resource')),
            ],
            options={
                'db_table': 'Resident',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('R', 'Resident'), ('O', 'Organization'), ('A', 'Admin')], max_length=1)),
                ('organization_name', models.CharField(max_length=50)),
                ('borrowed_resources', models.ManyToManyField(through='BorrowResource.BorrowResource', to='BorrowResource.resource')),
            ],
            options={
                'db_table': 'Organization',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=20)),
                ('user_type', models.CharField(choices=[('R', 'Resident'), ('O', 'Organization'), ('A', 'Admin')], max_length=1)),
                ('admin_status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
                ('approve_appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BookAppointment.appointment')),
                ('approve_borrowing', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BorrowResource.borrowresource')),
            ],
            options={
                'db_table': 'Admin',
            },
        ),
    ]

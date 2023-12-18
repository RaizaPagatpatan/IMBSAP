# Generated by Django 4.2.8 on 2023-12-14 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CreateAccount', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('eventID', models.BigAutoField(primary_key=True, serialize=False)),
                ('eventName', models.CharField(max_length=150)),
                ('details', models.CharField(max_length=250)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('event_status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('C', 'Cancelled')], max_length=1)),
                ('location', models.TextField()),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateAccount.organization')),
            ],
            options={
                'db_table': 'Event',
            },
        ),
    ]

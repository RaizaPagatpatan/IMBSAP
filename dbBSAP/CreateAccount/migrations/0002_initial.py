# Generated by Django 4.2.8 on 2023-12-14 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CreateAccount', '0001_initial'),
        ('OrganizeEvent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='approve_event',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='OrganizeEvent.event'),
        ),
    ]

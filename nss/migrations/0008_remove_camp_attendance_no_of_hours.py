# Generated by Django 5.0.6 on 2024-07-16 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nss', '0007_camp_alter_volunteer_blood_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp_attendance',
            name='no_of_hours',
        ),
    ]

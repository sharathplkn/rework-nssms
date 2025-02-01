# Generated by Django 5.0.6 on 2024-07-16 12:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nss', '0006_alter_programme_program_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('camp_id', models.AutoField(primary_key=True, serialize=False)),
                ('camp_name', models.CharField(max_length=40, null=True)),
                ('fromdate', models.DateField()),
                ('todate', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='community',
            field=models.CharField(choices=[('ST', 'ST'), ('SC', 'SC'), ('General', 'General'), ('OBC', 'OBC')], max_length=15),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='unit',
            field=models.IntegerField(choices=[('4', '4'), ('5', '5'), ('96', '96')]),
        ),
        migrations.CreateModel(
            name='Camp_Attendance',
            fields=[
                ('Attendance_id', models.AutoField(primary_key=True, serialize=False)),
                ('no_of_hours', models.IntegerField()),
                ('camp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nss.camp')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_attendances', to='nss.volunteer')),
            ],
        ),
        migrations.CreateModel(
            name='Camp_event_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_eventdetails', to='nss.event')),
            ],
        ),
        migrations.CreateModel(
            name='Camp_event_photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='events')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_eventphotos', to='nss.event')),
            ],
        ),
    ]

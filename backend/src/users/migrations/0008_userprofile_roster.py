# Generated by Django 3.2.23 on 2024-02-21 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffcalendar', '0008_remove_monthlyroster_employees'),
        ('users', '0007_remove_userprofile_shift'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='roster',
            field=models.ManyToManyField(to='staffcalendar.MonthlyRoster'),
        ),
    ]

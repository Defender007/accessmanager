# Generated by Django 3.2.23 on 2024-02-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_userprofile_shift'),
        ('staffcalendar', '0002_remove_shiftmanager_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyRoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_day', models.CharField(max_length=50)),
                ('employees', models.ManyToManyField(to='users.UserProfile')),
                ('shift', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='staffcalendar.shiftmanager')),
            ],
        ),
    ]

# Generated by Django 3.2.23 on 2024-02-18 13:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('staffcalendar', '0003_monthlyroster'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthlyroster',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monthlyroster',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2024, 2, 18, 13, 42, 33, 799679, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
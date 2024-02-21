# Generated by Django 3.2.23 on 2024-02-21 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staffcalendar', '0006_auto_20240221_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthlyroster',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='monthlyroster',
            name='start_date',
        ),
        migrations.AddField(
            model_name='monthlyroster',
            name='week_no',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]

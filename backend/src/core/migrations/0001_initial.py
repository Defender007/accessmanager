# Generated by Django 3.2.23 on 2024-01-15 17:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('swipe_count', models.IntegerField(default=0)),
                ('reader_uid', models.CharField(max_length=128)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('access_point', models.CharField(max_length=25)),
                ('raw_payload', models.JSONField()),
                ('door', models.CharField(max_length=128)),
                ('grant_type', models.CharField(max_length=25)),
            ],
        ),
    ]

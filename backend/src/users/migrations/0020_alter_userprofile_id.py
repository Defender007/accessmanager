# Generated by Django 3.2.23 on 2024-03-03 19:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_rename_staff_status_userprofile_employee_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
# Generated by Django 3.2.23 on 2024-03-02 11:31

from django.db import migrations, models
import utils.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_userprofile_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='employee_id',
            field=models.CharField(default=utils.utils.dummy_unique_str, max_length=128, unique=True),
        ),
    ]
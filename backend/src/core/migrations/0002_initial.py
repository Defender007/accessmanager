# Generated by Django 3.2.23 on 2024-01-15 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='authorizer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opener', to='users.userprofile'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_transactions', to='users.userprofile'),
        ),
    ]

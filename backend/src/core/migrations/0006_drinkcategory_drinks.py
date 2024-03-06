# Generated by Django 3.2.23 on 2024-03-05 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20240220_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.CharField(max_length=50)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.drinkcategory')),
            ],
        ),
    ]

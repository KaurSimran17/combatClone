# Generated by Django 4.0.4 on 2023-01-22 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_app', '0027_delete_additional_fighter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Additional_fighter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fight_name', models.CharField(max_length=100)),
                ('fight_weight', models.CharField(max_length=50)),
                ('wight_units', models.CharField(max_length=20)),
                ('fight_height', models.CharField(max_length=50)),
                ('height_units', models.CharField(max_length=20)),
                ('discipline', models.CharField(max_length=50)),
                ('gym_name', models.CharField(max_length=100)),
            ],
        ),
    ]
# Generated by Django 4.0.4 on 2023-01-25 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_app', '0030_remove_achivements_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='achivements',
            name='year',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
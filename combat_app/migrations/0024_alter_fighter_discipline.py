# Generated by Django 4.0.4 on 2023-01-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_app', '0023_rename_juzo_experience_martial_art_record_judo_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fighter',
            name='discipline',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
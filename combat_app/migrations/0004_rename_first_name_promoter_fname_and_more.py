# Generated by Django 4.0.4 on 2022-12-29 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat_app', '0003_alter_promoter_first_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promoter',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='promoter',
            old_name='last_name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='sanctioning',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='sanctioning',
            old_name='last_name',
            new_name='lname',
        ),
    ]
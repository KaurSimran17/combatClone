# Generated by Django 4.0.4 on 2023-01-04 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_app', '0008_rename_profile_img_promoter_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sanctioning',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
# Generated by Django 4.0.4 on 2023-01-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_app', '0021_muya_thai_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social_link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(max_length=500)),
                ('instagram', models.URLField(max_length=500)),
                ('twitter', models.URLField(max_length=500)),
                ('gmail', models.EmailField(max_length=300)),
            ],
        ),
    ]

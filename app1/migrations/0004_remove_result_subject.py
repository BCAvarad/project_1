# Generated by Django 5.1.4 on 2025-01-29 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_subject_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='subject',
        ),
    ]

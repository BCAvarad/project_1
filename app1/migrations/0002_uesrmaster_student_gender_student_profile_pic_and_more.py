# Generated by Django 5.1.4 on 2025-01-21 09:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uesrmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_pic',
            field=models.ImageField(default='none', upload_to='app1/templates/img/student'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('educetion', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('T_class', models.CharField(max_length=10)),
                ('Teacher_pic', models.ImageField(upload_to='app1/templates/img/teacher')),
                ('user_id', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
                ('t_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.uesrmaster')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='s_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.uesrmaster'),
        ),
    ]

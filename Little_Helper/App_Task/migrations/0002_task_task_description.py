# Generated by Django 4.2.1 on 2023-08-09 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
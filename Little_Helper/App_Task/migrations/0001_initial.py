# Generated by Django 4.2.1 on 2023-09-07 21:39

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=512)),
                ('task_date', models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 9, 7), message='Date cannot be in the past')])),
                ('task_time', models.TimeField()),
                ('task_description', models.TextField(blank=True, max_length=1000)),
                ('task_slug', models.SlugField(null=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['task_date', 'task_time'],
            },
        ),
    ]

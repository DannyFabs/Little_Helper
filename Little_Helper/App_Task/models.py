from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='all_tasks')
    task_name = models.CharField(max_length=512, blank=False)
    task_date = models.DateField(blank=False)
    task_time = models.TimeField(blank=False)
    task_description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.task_name

    class Meta:
        # this is an alternative order on how we want the blogs to be ordered
        ordering = ['task_date', 'task_time']

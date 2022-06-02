from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class Todolist(models.Model):
    title = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.title


class Todoitem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)

    def __str__(self):
        return f"{self.title}  : due {self.due_date}"

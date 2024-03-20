from django.db import models

# Create your models here.
class Tasks(models.Model):
    taskTitle=models.CharField(max_length=30)
    taskDesc=models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.taskTitle()
from django.db import models

class  Task(models.Model):
    taskTitle= models.CharField(max_length=30)
    taskdesc= models.TextField()
    time = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.taskTitle
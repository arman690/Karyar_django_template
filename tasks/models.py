from django.db import models
from django.utils import timezone



class TaskItem(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description =models.TextField(null= True,blank=True)
    due_date =models.DateField(default= timezone.now)
    completed =models.BooleanField(default= True)

    def __str__(self):
        return f'{self.title}'



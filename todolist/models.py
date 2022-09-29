from django.db import models
from django.contrib.auth.models import User

class ToDoList(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
    date_of_task = models.DateField()
    title = models.TextField()
    description = models.TextField()

    


from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    """
    defining the DB model structure of Todo 
    """
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

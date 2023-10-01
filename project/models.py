from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    added_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

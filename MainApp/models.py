from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Fruit(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    taste=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return self.name
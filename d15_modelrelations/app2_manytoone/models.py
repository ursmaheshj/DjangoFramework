from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    publish = models.DateField()
    def __str__(self):
        return self.title
    
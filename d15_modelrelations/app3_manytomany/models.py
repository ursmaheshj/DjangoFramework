from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    

class Song(models.Model):
    title = models.CharField(max_length=50)
    duration = models.IntegerField()
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.title
    
    def singer(self):
        return ', '.join([str(s) for s in self.user.all()])
    
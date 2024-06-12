from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    
class Page(models.Model):
    pagename = models.CharField(max_length=50)
    publish = models.DateField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.pagename
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    publish = models.DateField()
    publish_in = models.OneToOneField(Page,models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    

class Song(models.Model):
    name = models.CharField(max_length=50)
    duration = models.FloatField()
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name
    def sung_by(self):
        return ', '.join([str(s) for s in self.user.all()])
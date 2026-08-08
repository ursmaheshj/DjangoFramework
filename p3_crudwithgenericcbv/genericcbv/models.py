from django.db import models
from django.urls import reverse_lazy

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30,unique=True)
    age = models.IntegerField(max_length=3)
    password = models.CharField(max_length=30)

    # def get_absolute_url(self):
    #     return reverse_lazy('detailuser',kwargs={'pk':self.pk})
from django.db import models

# Create your models here.
class Husband(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    def __str__(self):
        return self.name
    

class Wife(models.Model):
    name = models.CharField(max_length=50)
    husband = models.OneToOneField(Husband,on_delete=models.PROTECT)
    def __str__(self):
        return self.name
    
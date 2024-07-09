from django.db import models
from django.urls import reverse

# Create your models here.
class Cstudent(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    course = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse("createdetailview", kwargs={"pk": self.pk})
    
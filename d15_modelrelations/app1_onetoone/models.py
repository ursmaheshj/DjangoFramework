from django.db import models

# Create your models here.
class Husband(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    def __str__(self):
        return self.name
    

class Wife(models.Model):
    name = models.CharField(max_length=50)
    # husband = models.OneToOneField(Husband,on_delete=models.PROTECT,limit_choices_to={'salary':5000})
    husband = models.OneToOneField(Husband,on_delete=models.CASCADE,limit_choices_to={'salary':5000})
    def __str__(self):
        return self.name
    


#-------------Models to understand Model inheritance 
class UserModel(models.Model):
    name = models.CharField(max_length=50)
    is_staff = models.BooleanField()
    def __str__(self):
        return self.name
    

class Page(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(UserModel,on_delete=models.CASCADE,primary_key=True)
    publish = models.DateField()
    def __str__(self):
        return self.name
    

class Like(Page):
    panna = models.OneToOneField(Page,on_delete=models.CASCADE,primary_key=True,parent_link=True)
    likes = models.IntegerField()
    def __str__(self):
        return self.name
    
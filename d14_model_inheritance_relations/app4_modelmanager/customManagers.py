from django.db import models

class CustomManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().order_by('name')
    
    def get_salary_range(self,s1,s2):
        return super().get_queryset().filter(salary__range=(s1,s2))
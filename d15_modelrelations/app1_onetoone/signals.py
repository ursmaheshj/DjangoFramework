from app1_onetoone.models import Husband,Wife
from django.db.models.signals import post_delete
from django.dispatch import receiver

#creating singal to delete husband when wife is deleted

@receiver(post_delete,sender=Wife)
def delete_husband(sender,instance,**kwargs):
    print(f'{instance.husband} is deleted')
    instance.husband.delete()

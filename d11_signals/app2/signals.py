from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in,sender=User)
def logged_in(sender,request,user,**kwargs):
    lc = cache.get('loginCount',0,version=user.pk)
    newCount = lc + 1
    cache.set('loginCount',newCount,60*60*24,version=user.pk)
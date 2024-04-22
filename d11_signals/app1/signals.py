from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in)
def login_success(sender,request,user,**kwargs):
    print('---------------------------------------')
    print('----------- -Logged in Signal----------')
    print('Sender:',sender)
    print('Request:',request)
    print('User:',user)
    print('User Password:',user.password)
    print('Kwargs',kwargs)

@receiver(user_logged_out)
def login_success(sender,request,user,**kwargs):
    print('---------------------------------------')
    print('------------Logged out Signal----------')
    print('Sender:',sender)
    print('Request:',request)
    print('User:',user)
    print('User Password:',user.password)
    print('Kwargs',kwargs)

@receiver(user_login_failed)
def login_success(sender,credentials,request,**kwargs):
    print('---------------------------------------')
    print('----------- -Logged in Failed----------')
    print('Sender:',sender)
    print('Request:',request)
    # print('User:',user)
    print('credentials:',credentials)
    print('Kwargs',kwargs)

#Manual Signal Connection
# user_logged_in.connect(login_success,sender=User,dispatch_uid='SuccessSignal')
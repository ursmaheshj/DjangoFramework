from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save


# -----------------------------login/logout Signals-------------------------------
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


#--------------------------------------Model signals-----------------------

@receiver(pre_save,sender=User)
def at_beginning_save(sender,instance,**kwargs):
    print('---------------------------------------')
    print('-------------Beginning of Save----------')
    print('Sender:',sender)
    print('Instance:',instance)
    print('kwargs:',kwargs)

@receiver(post_save,sender=User)
def at_ending_save(sender,instance,created,**kwargs):
    if created:
        print('---------------------------------------')
        print('-------------Ending of Save----------')
        print('Sender:',sender)
        print('Instance:',instance)
        print('created:',created)
        print('kwargs:',kwargs)
    else:
        print('---------------------------------------')
        print('-------------Ending of Save----------')
        print('Sender:',sender)
        print('Instance:',instance)
        print('created:',created)
        print('kwargs:',kwargs)

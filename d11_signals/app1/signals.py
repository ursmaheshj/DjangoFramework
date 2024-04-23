from django.contrib.auth.models import User
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.core.signals import request_started,request_finished,got_request_exception
from django.db.models.signals import pre_migrate,post_migrate



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


@receiver(pre_delete)
def at_beginning_delete(sender,instance,**kwargs):
    print('---------------------------------------')
    print('-------------Beginning of delete----------')
    print('Sender:',sender)
    print('Instance:',instance)
    print('kwargs:',kwargs)

@receiver(post_delete)
def at_ending_delete(sender,instance,**kwargs):
    print('---------------------------------------')
    print('-------------Ending of delete----------')
    print('Sender:',sender)
    print('Instance:',instance)
    print('kwargs:',kwargs)

#-----------------------------------Request/Response signals----------------------------

@receiver(request_started)
def req_start(sender,environ,**kwargs):
    print('---------------------------------------')
    print('-------------At start request----------')
    print('Sender:',sender)
    print('environ:',environ)
    print('kwargs:',kwargs)

@receiver(request_finished)
def req_finish(sender,**kwargs):
    print('---------------------------------------')
    print('-------------At request finished----------')
    print('Sender:',sender)
    print('kwargs:',kwargs)

@receiver(got_request_exception)
def req_exception(sender,request,**kwargs):
    print('---------------------------------------')
    print('-------------At request exception----------')
    print('Sender:',sender)
    print('request:',request)
    print('kwargs:',kwargs)


#------------------------------------Management Signals---------------------
@receiver(pre_migrate)
def before_migrate_app(sender, app_config, verbosity, interactive,using,plan,apps,**kwargs):
    print('---------------------------------------')
    print('-------------Before Migration----------')
    print('Sender:',sender)
    print('app_config:',app_config)
    print('verbosity:',verbosity)
    print('interactive:',interactive)
    print('using:',using)
    print('apps:',apps)
    print('kwargs:',kwargs)

@receiver(pre_migrate)
def after_migrate_app(sender, app_config, verbosity, interactive,using,plan,apps,**kwargs):
    print('---------------------------------------')
    print('-------------After Migration-----------')
    print('Sender:',sender)
    print('app_config:',app_config)
    print('verbosity:',verbosity)
    print('interactive:',interactive)
    print('using:',using)
    print('apps:',apps)
    print('kwargs:',kwargs)


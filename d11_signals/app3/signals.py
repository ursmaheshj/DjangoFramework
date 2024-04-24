from django.dispatch import Signal,receiver

notification = Signal()

@receiver(notification)
def sendNotification(sender,**kwargs):
    print('-----------------CustomSignal---------------------')
    print('sender-',sender)
    print('kwargs-',kwargs)

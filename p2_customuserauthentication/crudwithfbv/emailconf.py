from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import threading

class SendEmailThread(threading.Thread):
    def __init__(self,email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()
# Using thread will run this asynchronously by creating new thread
# in background so if error happens still view will run as usual
# without any issue
def send_activation_email(recipient_email,activation_url):
    try:
        subject = "Activate your account on" + settings.SITE_NAME
        from_email = "noreply@demomailtrap.co"
        to_email = [recipient_email]

        context = {
            'user': recipient_email,
            'activation_url': activation_url,
            'domain': settings.SITE_DOMAIN,
            'site_name': settings.SITE_NAME,
            'valid_days': 3, # Default Django token validity
        }
        html_content = render_to_string('crudwithfbv/emailtemplate.html',context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(subject,text_content,from_email,to_email)
        email.attach_alternative(html_content,'text/html')
        # SendEmailThread(email).start()
    except Exception as e:
        raise Exception(f"Issue while sending activation mail: {e}")
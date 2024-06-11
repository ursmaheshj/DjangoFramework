from django.apps import AppConfig


class App1OnetooneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app1_onetoone'

    def ready(self):
        import app1_onetoone.signals
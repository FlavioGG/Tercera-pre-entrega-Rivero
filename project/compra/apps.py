from django.apps import AppConfig


class ClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cliente'

class PaisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'país'    
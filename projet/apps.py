from django.apps import AppConfig

class ProjetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projet'

    def ready(self):
        import projet.signals  # Importer les signaux
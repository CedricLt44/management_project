from django.db.models.signals import post_delete
from django.dispatch import receiver
import os
from .models import ProjectFile

#pour suppressions des fichiers dans media 

@receiver(post_delete, sender=ProjectFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Supprime le fichier associé lorsqu'un objet ProjectFile est supprimé.
    """
    if instance.attachment and os.path.isfile(instance.attachment.path):
        os.remove(instance.attachment.path)

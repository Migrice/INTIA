# users/management/commands/create_dg.py
import os
from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = "Créer le compte DG initial"

    def handle(self, *args, **kwargs):
        # dg_password = os.environ.get('DG_PASSWORD')
        # dg_username = os.environ.get("DG_USERNAME")
        # dg_email = os.environ.get("DG_EMAIL")
        # if not dg_password:
        #     self.stdout.write(self.style.ERROR('Variable d\'environnement DG_PASSWORD non définie'))
        #     return

        if User.objects.filter(role="DG").exists():
            self.stdout.write(self.style.WARNING("Un DG existe déjà."))
        else:
            User.objects.create_superuser(
                username="ADMIN",
                email="insia.contact@gmail.com",
                password="PAS12Mn",
                role="DG",
            )
            self.stdout.write(self.style.SUCCESS("Compte DG créé avec succès."))

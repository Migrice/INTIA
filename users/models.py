from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date, datetime


class Branch(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.city}"


class User(AbstractUser):
    ROLE_CHOICES = [
        ("DG", "Directeur Général"),
        ("RESPONSABLE", "Responsable Succursale"),
        ("AGENT", "Agent"),
        ("EXPERT", "Expert Sinistre"),
        ("COMPTABLE", "Comptable"),
        ("CLIENT", "Client"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="users_user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="users_user_permissions",
        related_query_name="user",
    )

    def is_dg(self):
        return self.role == "DG"

    def is_responsable(self):
        return self.role == "RESPONSABLE"

    def is_agent(self):
        return self.role == "AGENT"

    def is_expert(self):
        return self.role == "EXPERT"

    def is_comptable(self):
        return self.role == "COMPTABLE"

    def is_client(self):
        return self.role == "CLIENT"


class Customer(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_name="customer_set",
        related_query_name="customer",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        related_name="customer_permissions_set",  # Unique related_name
        related_query_name="customer_permission",
    )

    class Meta:
        # ... your other Meta options ...
        pass

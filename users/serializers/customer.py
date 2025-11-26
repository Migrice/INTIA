from rest_framework import serializers

from users.models import Customer, User


class CreateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "address",
            "username",
        ]
        read_only_fields = ["id"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["id", "email", "first_name", "last_name", "phone", "address"]
        read_only_fields = ["id"]

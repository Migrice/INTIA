from rest_framework import serializers

from users.models import Branch


class CreateBranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ["id", "name", "city", "address", "phone"]
        read_only_fields = ["id"]

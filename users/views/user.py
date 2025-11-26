from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from users.models import Branch, Customer, User
from users.serializers.branch import CreateBranchSerializer
from users.serializers.customer import CreateCustomerSerializer, CustomerSerializer
from users.serializers.user import UserSerializer


class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDeleteUserView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

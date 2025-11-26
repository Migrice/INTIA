from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions

from users.models import Branch, Customer
from users.serializers.branch import CreateBranchSerializer
from users.serializers.customer import CreateCustomerSerializer, CustomerSerializer


class ListCreateCustomerView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer

    permission_classes = [permissions.IsAuthenticated]


from rest_framework import mixins
from rest_framework.generics import GenericAPIView


class RetrieveUpdateDeleteCustomerView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView,
):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

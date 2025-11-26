
from rest_framework.generics import ListCreateAPIView

from users.models import Branch
from users.serializers.branch import CreateBranchSerializer

class ListCreateBranchView(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = CreateBranchSerializer


    def list(self):
        return Branch
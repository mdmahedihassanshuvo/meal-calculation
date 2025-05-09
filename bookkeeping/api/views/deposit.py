# REST_FRAMEWORK IMPORTS
from rest_framework.generics import ListCreateAPIView

# LOCAL IMPORTS
from bookkeeping.models import Deposit
from bookkeeping.api.serializer import DepositSerializers


class DepositListCreateAPIView(ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializers

    def get_queryset(self):
        queryset = Deposit.objects.all()
        member_id = self.request.query_params.get('member_id')
        if member_id:
            queryset = queryset.filter(name_id=member_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save()

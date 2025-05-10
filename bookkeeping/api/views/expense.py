# REST_FRAMEWORK IMPORTS
from rest_framework.generics import ListCreateAPIView

# LOCAL IMPORTS
from bookkeeping.models import Expense
from bookkeeping.api.serializer import ExpenseSerializers


class ExpenseListCreateAPIView(ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializers

    def get_queryset(self):
        queryset = Expense.objects.all()
        member_id = self.request.query_params.get('member_id')
        if member_id:
            queryset = queryset.filter(name_id=member_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save()

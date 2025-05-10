# REST_FRAMEWORK IMPORTS
from rest_framework.generics import ListCreateAPIView

# LOCAL IMPORTS
from bookkeeping.models import Meal
from bookkeeping.api.serializer import MealSerializers


class MealListCreateAPIView(ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers

    def get_queryset(self):
        queryset = Meal.objects.all()
        member_id = self.request.query_params.get('member_id')
        if member_id:
            queryset = queryset.filter(name_id=member_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save()

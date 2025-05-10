# REST_FRAMEWORK IMPORTS
from rest_framework import serializers

# LOCAL IMPORTS
from bookkeeping.models import Expense


class ExpenseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'member',
            'amount',
            'expense_date'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['member'] = instance.member.name if instance.member else None # noqa
        return representation

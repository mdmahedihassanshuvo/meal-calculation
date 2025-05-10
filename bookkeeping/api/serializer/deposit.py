# REST_FRAMEWORK IMPORTS
from rest_framework import serializers

# LOCAL IMPORTS
from bookkeeping.models import Deposit


class DepositSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = [
            'id',
            'member',
            'amount',
            'deposite_date'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['member'] = instance.member.name if instance.member else None # noqa
        return representation

# REST_FRAMEWORK IMPORTS
from rest_framework import serializers

# LOCAL IMPORTS
from bookkeeping.models import Deposit


class DepositSerializers(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = [
            'id',
            'member'
            'amount',
            'deposite_date'
        ]

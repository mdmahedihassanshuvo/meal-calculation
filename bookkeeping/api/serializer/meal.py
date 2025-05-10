# REST_FRAMEWORK IMPORTS
from rest_framework import serializers

# LOCAL IMPORTS
from bookkeeping.models import Meal


class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = [
            'id',
            'member',
            'meal_date',
            'meal_count'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['member'] = instance.member.name if instance.member else None # noqa
        return representation

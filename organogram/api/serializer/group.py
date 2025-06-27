# REST_FRAMWORK IMPORTS
from rest_framework import serializers

# LOCAL IMPORTS
from organogram.models import Group


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

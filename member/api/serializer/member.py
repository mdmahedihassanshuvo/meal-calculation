# REST_FRAMEWORK IMPORTS
from rest_framework import serializers

# LOCAL IMPORTS
from member.models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = [
            'id',
            'name',
            'nickname'
        ]

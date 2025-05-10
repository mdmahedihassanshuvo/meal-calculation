# DJANGO IMPORTS
from django.db.models import Q

# REST_FRAMEWORK IMPORTS
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

# LOCAL IMPORTS
from member.models import Member
from member.api.serializer import MemberSerializer


class MemberListCreateAPIView(ListCreateAPIView):
    serializer_class = MemberSerializer

    def get_queryset(self):
        queryset = Member.objects.all()
        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(
                    name__icontains=search_query
                ) | Q(
                    nickname__icontains=search_query
                )
            )
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

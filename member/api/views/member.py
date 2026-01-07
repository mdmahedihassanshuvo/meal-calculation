# DJANGO IMPORTS
from django.db.models import Q

# REST_FRAMEWORK IMPORTS
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

# LOCAL IMPORTS
from member.models import Member
from organogram.models import Group
from member.api.serializer import MemberSerializer

class GroupMemberListApiView(ListAPIView):
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        search_query = self.request.GET.get('search', None)

        if user.is_superuser or user.has_perm('organogram.member_management'):
            queryset = Member.objects.all().distinct()
        else:
            # Get all groups created by this user
            groups = Group.objects.filter(created_by=user)
            # Get all members in those groups
            queryset = Member.objects.filter(
                groups__in=groups
            ).distinct()
            print(f"{'*' * 20}")
            print("Filtered Members:", queryset)

        # Apply search filter if provided
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(nickname__icontains=search_query)
            )

        return queryset

class MemberListCreateAPIView(ListCreateAPIView):
    serializer_class = MemberSerializer
    parser_classes = [MultiPartParser, FormParser]

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

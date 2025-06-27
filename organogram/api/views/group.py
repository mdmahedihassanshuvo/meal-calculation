# REST_FRAMWORK IMPORTS
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

# DJANGO IMPORTS
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group as AuthGroup

# LOCAL IMPORTS
from organogram.models import Group
from organogram.api.serializer import GroupSerializer
from rest_framework.permissions import IsAuthenticated
from member.models import Member


class GroupDestroyAPIView(DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        group = get_object_or_404(Group, pk=kwargs.get('pk'))

        # Check permission
        if request.user.is_superuser or group.created_by == request.user:
            creator = group.created_by

            if creator:
                try:
                    creator_member = Member.objects.get(user=creator)
                    creator_member.is_manager = False
                    creator_member.is_member = True
                    creator_member.save()
                except Member.DoesNotExist:
                    pass

                try:
                    manager_group = AuthGroup.objects.get(name='manager')
                    other_managed_groups = Group.objects.filter(created_by=creator).exclude(pk=group.pk) # noqa
                    if not other_managed_groups.exists():
                        creator.groups.remove(manager_group)
                except AuthGroup.DoesNotExist:
                    pass

            group.delete()
            return Response({"message": "Group deleted successfully"}, status=status.HTTP_200_OK) # noqa

        else:
            return Response({"message": "Permission denied"}, status=status.HTTP_403_FORBIDDEN) # noqa

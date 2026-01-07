# DJANGO IMPORTS
from django.urls import path

# LOCAL IMPORTS
from member.api.views import MemberListCreateAPIView, GroupMemberListApiView

urlpatterns = [
    path(
        'add-member/',
        MemberListCreateAPIView.as_view(),
        name='add_member'
    ),
    path(
        'member-list/',
        MemberListCreateAPIView.as_view(),
        name='member_list'
    ),
    path(
        'group-member-list/',
        GroupMemberListApiView.as_view(),
        name='group_member_list'
    )
]

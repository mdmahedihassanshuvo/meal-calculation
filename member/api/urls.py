# DJANGO IMPORTS
from django.urls import path

# LOCAL IMPORTS
from member.api.views import MemberListCreateAPIView

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
]

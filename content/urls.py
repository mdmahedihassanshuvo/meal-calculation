from django.urls import path
from content.views import (
    MemberListView,
    MemberDetailsView
)

app_name = 'content'

urlpatterns = [
    path(
        'member-list/',
        MemberListView.as_view(),
        name='member_list'
    ),
    path(
        'member-details/<int:pk>/',
        MemberDetailsView.as_view(),
        name='member_details'
    ),
]

# organogram/urls.py

from django.urls import path
from organogram.views import group

app_name = 'organogram'

urlpatterns = [
    path(
        'groups/',
        group.GroupListView.as_view(),
        name='group_list'
    ),
    path(
        'groups/create/',
        group.GroupCreateView.as_view(),
        name='group_create'
    ),
    path(
        'groups/<int:pk>/details',
        group.GroupMemberListView.as_view(),
        name='group_details'
    ),
]

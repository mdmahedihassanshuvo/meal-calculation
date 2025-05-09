from django.urls import path
from content.views import (
    MemberTemplateView, MemberListView
)

app_name = 'content'

urlpatterns = [
    path(
        'member/',
        MemberTemplateView.as_view(),
        name='member'
    ),
    path(
        'member-list/',
        MemberListView.as_view(),
        name='member_list'
    ),
]

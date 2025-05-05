from django.urls import path
from content.views import MemberTemplateView

urlpatterns = [
    path(
        'member/',
        MemberTemplateView.as_view(),
        name='member'
    ),
]

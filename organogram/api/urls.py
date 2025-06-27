# DJANGO IMPORTS
from django.urls import path

# LOCAL IMPORTS
from organogram.api.views import (
    GroupDestroyAPIView
)

urlpatterns = [
    path(
        'group-delete/<int:pk>/',
        GroupDestroyAPIView.as_view(),
        name='group_delete'
    ),
]

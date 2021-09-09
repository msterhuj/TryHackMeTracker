from rest_framework import viewsets

from server.api.models.TrackedUser import TrackedUser
from server.api.permissions.AppPermission import AppPermission
from server.api.serializer import TrackedUserSerializer


class TrackedUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TrackedUser to be viewed or edited.
    """
    queryset = TrackedUser.objects.all().order_by("-id")
    serializer_class = TrackedUserSerializer
    permission_classes = [AppPermission]

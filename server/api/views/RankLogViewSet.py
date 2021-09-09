from rest_framework import viewsets

from server.api.models.RankLog import RankLog
from server.api.permissions.AppPermission import AppPermission
from server.api.serializer import RankLogSerializer


class TrackedUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TrackedUser to be viewed or edited.
    """
    queryset = RankLog.objects.all().order_by("-id")
    serializer_class = RankLogSerializer
    permission_classes = [AppPermission]

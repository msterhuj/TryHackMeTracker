from rest_framework import serializers

from server.api.models.TrackedUser import TrackedUser
from server.api.models.RankLog import RankLog


class TrackedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrackedUser
        fields = ["url", "name", "best_rank", "created_at", "last_update"]


class RankLogSerializer(serializers.HyperlinkedModelSerializer):
    tracked_user = serializers.StringRelatedField(many=True)

    class Meta:
        model = RankLog
        fields = ["url", "tracked_user", "rank", "created_at", "last_update"]

from django.db import models

from server.api.models.TrackedUser import TrackedUser


class RankLog(models.Model):
    tracked_user = models.ForeignKey(TrackedUser, on_delete=models.CASCADE)
    rank = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.tracked_user, self.rank)

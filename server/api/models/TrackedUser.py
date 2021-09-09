from django.db import models


class TrackedUser(models.Model):
    name = models.CharField(unique=True, max_length=255)
    best_rank = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

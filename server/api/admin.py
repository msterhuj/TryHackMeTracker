from django.contrib import admin

from server.api.models.TrackedUser import TrackedUser
from server.api.models.RankLog import RankLog

# Register your models here.
admin.site.register(TrackedUser)
admin.site.register(RankLog)

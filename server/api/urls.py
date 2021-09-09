from django.urls import path, include
from rest_framework import routers

from server.api.views.TrackedUserViewSet import TrackedUserViewSet

from django.http import HttpRequest
from django.shortcuts import render


def browsable_API(request: HttpRequest):
    return render(request, 'browsable.html')


router = routers.DefaultRouter()
router.register(r'user', TrackedUserViewSet)

urlpatterns = [
    path('browsable', browsable_API, name="browsable_api"),
    path('', include(router.urls))
]

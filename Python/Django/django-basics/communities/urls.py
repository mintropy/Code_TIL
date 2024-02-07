from django.urls import path

from communities.views import CommunityAPI

urlpatterns = [
    path("", CommunityAPI.as_view(), name="community_list"),  # type: ignore
]

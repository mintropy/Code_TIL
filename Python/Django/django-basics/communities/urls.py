from django.urls import path

from communities.views import AdminCommunityAPI, CommunityAPI, UserCommunityAPI

urlpatterns = [
    path("", CommunityAPI.as_view(), name="community_list"),
    path("admin/", AdminCommunityAPI.as_view(), name="community_list"),
    path("user/", UserCommunityAPI.as_view(), name="community_list"),
]

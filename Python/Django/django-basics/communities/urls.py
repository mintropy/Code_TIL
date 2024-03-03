from django.urls import path

from communities.views import (
    AdminCommunityAPI,
    AdminPostAPI,
    CommunityAPI,
    PopularPostAPI,
    PostAPI,
    UserCommunityAPI,
)

urlpatterns = [
    path("", CommunityAPI.as_view(), name="community_list"),
    path("admin/", AdminCommunityAPI.as_view(), name="community_list"),
    path("user/", UserCommunityAPI.as_view(), name="community_list"),
    path("<str:community_id>/posts/", PostAPI.as_view(), name="community_detail"),
    path(
        "<str:community_id>/posts/popular/",
        PopularPostAPI.as_view(),
        name="community_detail",
    ),
    path(
        "<str:community_id>/posts/admin/",
        AdminPostAPI.as_view(),
        name="community_detail",
    ),
]

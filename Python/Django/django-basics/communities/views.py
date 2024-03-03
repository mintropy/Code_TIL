from datetime import datetime, timedelta

from django.db.models import BooleanField, Case, Count, Max, When
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from communities.models import AdminPost, Community, PopularPost, Post
from communities.serializesrs import (
    AdminPostSerializer,
    CommunitySerializer,
    PostSerializer,
)


class CommunityAPI(APIView, PageNumberPagination):  # type: ignore
    def get(self, request: Request) -> Response:
        seven_days_ago = datetime.now() - timedelta(days=7)

        communities = (
            Community.objects.all()
            .annotate(
                post_count=Count("posts"),
                latest_post=Max("posts__created_at"),
                new_community=Case(
                    When(created_at__gte=seven_days_ago, then=True),
                    default=False,
                    output_field=BooleanField(),
                ),
            )
            .order_by("-created_at")
        )

        paginated_communities = self.paginate_queryset(communities, request, view=self)
        serializer = CommunitySerializer(paginated_communities, many=True)
        return self.get_paginated_response(serializer.data)


class AdminCommunityAPI(APIView, PageNumberPagination):  # type: ignore
    def get(self, request: Request) -> Response:

        communities = (
            Community.objects.all()
            .annotate(
                post_count=Count("posts"),
                latest_post=Max("posts__created_at"),
            )
            .order_by("-created_at")
        )

        paginated_communities = self.paginate_queryset(communities, request, view=self)
        serializer = CommunitySerializer(
            paginated_communities, many=True, context="admin"
        )
        return self.get_paginated_response(serializer.data)


class UserCommunityAPI(APIView, PageNumberPagination):  # type: ignore
    def get(self, request: Request) -> Response:
        seven_days_ago = datetime.now() - timedelta(days=7)

        communities = (
            Community.objects.all()
            .annotate(
                latest_post=Max("posts__created_at"),
                new_community=Case(
                    When(created_at__gte=seven_days_ago, then=True),
                    default=False,
                    output_field=BooleanField(),
                ),
            )
            .order_by("-created_at")
        )

        paginated_communities = self.paginate_queryset(communities, request, view=self)
        serializer = CommunitySerializer(
            paginated_communities, many=True, context="user"
        )
        return self.get_paginated_response(serializer.data)


class PostAPI(APIView, PageNumberPagination):  # type: ignore
    def get(self, request: Request, community_id: str) -> Response:
        print(community_id, type(community_id))
        community = get_object_or_404(Community, id=community_id)
        posts = Post.objects.filter(community=community)
        paginated_posts = self.paginate_queryset(posts, request, view=self)
        serializer = PostSerializer(paginated_posts, many=True)
        return self.get_paginated_response(serializer.data)


class PopularPostAPI(APIView, PageNumberPagination):  # type: ignore
    def get(self, request: Request, community_id: str) -> Response:
        community = get_object_or_404(Community, id=community_id)
        popular_posts = PopularPost.objects.filter(community=community)
        paginated_posts = self.paginate_queryset(popular_posts, request, view=self)
        serializer = PostSerializer(paginated_posts, many=True)
        return self.get_paginated_response(serializer.data)


class AdminPostAPI(APIView, PageNumberPagination):  # type: ignore
    def get(self, request: Request, community_id: str) -> Response:
        community = get_object_or_404(Community, id=community_id)
        posts = AdminPost.objects.filter(community=community)
        fixed = request.query_params.get("fixed")
        if fixed == "f":
            posts = posts.filter(fixed=True)
        elif fixed == "t":
            posts = posts.filter(fixed=False)
        elif fixed == "all":
            pass
        else:
            return Response({"error": "invalid query parameter"}, status=400)
        posts = posts.order_by("-created_at")
        paginated_posts = self.paginate_queryset(posts, request, view=self)
        serializer = AdminPostSerializer(paginated_posts, many=True)
        return self.get_paginated_response(serializer.data)

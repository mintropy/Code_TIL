from datetime import datetime, timedelta

from django.db.models import BooleanField, Case, Count, Max, When
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from communities.models import Community
from communities.serializesrs import CommunitySerializer


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


class UserCommunityAPI(APIView, PageNumberPagination):  # type: ignore
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

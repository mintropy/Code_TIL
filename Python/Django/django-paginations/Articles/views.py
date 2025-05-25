from rest_framework import filters, generics, pagination, serializers

from Articles.models import Article


class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100


class CustomLimitOffsetPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class CustomCursorPagination(pagination.CursorPagination):
    page_size = 10
    max_page_size = 100
    ordering = "-created_at"


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class ArticleView(generics.ListAPIView):
    """
    API view to retrieve a list of articles.
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPageNumberPagination

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at", "views", "likes"]

    # def get_queryset(self):
    #     ordering = self.request.GET.get("ordering", "created_at")
    #     if ordering == "views":
    #         return self.queryset.order_by("-views")
    #     elif ordering == "likes":
    #         return self.queryset.order_by("-likes")
    #     return self.queryset.order_by("-created_at")

    def get(self, request, *args, **kwargs):
        if "limit" in request.GET or "offset" in request.GET:
            self.pagination_class = CustomLimitOffsetPagination
        elif "cursor" in request.GET:
            self.pagination_class = CustomCursorPagination

        return super().get(request, *args, **kwargs)

from django.urls import path

from Articles.views import ArticleView

urlpatterns = [
    path("", ArticleView.as_view(), name="article_list"),
]

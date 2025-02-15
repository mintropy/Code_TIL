from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("community/", include("communities.urls")),
    path("todo/", include("todos.urls")),
]

urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]

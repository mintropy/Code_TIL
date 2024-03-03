from rest_framework import serializers

from communities.models import AdminPost, Community, Post


class CommunitySerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)
    latest_post = serializers.DateTimeField(read_only=True)
    new_community = serializers.BooleanField(read_only=True)

    class Meta:
        model = Community
        fields = "__all__"

    def __init__(self, *args, **kwargs) -> None:
        context = kwargs.get("context", None)
        super().__init__(*args, **kwargs)
        exclude_fields = []
        if context == "admin":
            exclude_fields = ["new_community"]
        elif context == "user":
            exclude_fields = ["post_count", "created_at", "updated_at"]
        print(self.fields)
        for field_name in exclude_fields:
            self.fields.pop(field_name)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "content", "likes"]


class AdminPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminPost
        fields = ["id", "title", "content", "likes", "fixed"]

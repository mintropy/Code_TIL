from rest_framework import serializers

from communities.models import Community


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
        if context == "admin":
            pass
        elif context == "user":
            pass

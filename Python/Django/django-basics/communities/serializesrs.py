from rest_framework import serializers

from communities.models import Community


class CommunitySerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)
    latest_post = serializers.DateTimeField(read_only=True)
    new_community = serializers.BooleanField(read_only=True)

    class Meta:
        model = Community
        fields = "__all__"

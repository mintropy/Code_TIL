from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class CommunityAPI(APIView):
    def get(self, request: Request) -> Response:
        return Response(status=status.HTTP_200_OK)

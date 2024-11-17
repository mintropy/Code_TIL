from rest_framework.response import Response
from rest_framework.views import APIView

from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoAPI(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TodoPriorityAPI(APIView):
    def get(self, request, priority):
        print(priority)
        todos = Todo.objects.filter(priority=priority)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

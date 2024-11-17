from django.urls import path, register_converter

from todos.views import TodoAPI, TodoPriorityAPI


class NegativeIntConverter:
    regex = "-?\d+"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%d" % value


register_converter(NegativeIntConverter, "negint")

urlpatterns = [
    path("", TodoAPI.as_view(), name="todo_list"),
    path(
        "priority/<negint:priority>/", TodoPriorityAPI.as_view(), name="todo_priority"
    ),
]

import graphene
from graphene_django.types import DjangoObjectType

from books.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"


class Query(graphene.ObjectType):
    books = graphene.List(BookType)

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book_by_name(self, info, name):
        return Book.objects.get(name=name)


schema = graphene.Schema(query=Query)

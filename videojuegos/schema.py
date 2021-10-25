import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from videojuegos.models import Category, Videojuego


# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'videojuegos']
        interfaces = (relay.Node, )

# Se hace lo mismo con el modelo Ingredient
class VideojuegoNode(DjangoObjectType):
    class Meta:
        model = Videojuego
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    videojuego = relay.Node.Field(VideojuegoNode)
    all_videojuegos = DjangoFilterConnectionField(VideojuegoNode)

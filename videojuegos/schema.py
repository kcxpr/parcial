import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from videojuegos.models import Videojuego

from graphql_relay.node.node import from_global_id
# Graphene automáticamente mapeara los campos del modelo Category en un nodo CategoryNode.
# Esto se configura en la Meta clase 

# Se hace lo mismo con el modelo Ingredient
class VideojuegoNode(DjangoObjectType):
    class Meta:
        model = Videojuego
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
           
        }
        interfaces = (relay.Node, )

class CreateVideojuego(graphene.relay.ClientIDMutation):
    videojuego = graphene.Field(VideojuegoNode)
    class Input:
        name = graphene.String()
        notes = graphene.String()
    def mutate_and_get_payload(root, info, **input):
        videojuego = Videojuego(
            name=input.get('name'),
            notes=input.get('notes'),
        )
        videojuego.save()
        return CreateVideojuego(videojuego=videojuego)

class UpdateVideojuego(graphene.relay.ClientIDMutation):
    videojuego = graphene.Field(VideojuegoNode)
    class Input:
        id = graphene.String()
        name = graphene.String()
        notes= graphene.String()
    def mutate_and_get_payload(root, info, **input):
        videojuego = Videojuego.objects.get(pk=from_global_id(input.get('id'))[1])
        videojuego.name = input.get('name')
        videojuego.notes = input.get('notes')
        videojuego.save()
        return UpdateVideojuego(videojuego=videojuego)
class Query(graphene.ObjectType):
   
    videojuego = relay.Node.Field(VideojuegoNode)
    all_videojuegos = DjangoFilterConnectionField(VideojuegoNode)

class Mutation(graphene.AbstractType):
    create_videojuego = CreateVideojuego.Field()
    update_videojuego = UpdateVideojuego.Field()
import graphene
from graphene_django import DjangoObjectType
#como estamos dentro de la carpeta cookbook, pero los modelos estan en la carpetea ingredients
#necesitamos regresar un nivel de carpete por eso agregamos el ".."  al path actual
import sys
sys.path.append("..")
import videojuegos.schema


class Query(videojuegos.schema.Query, graphene.ObjectType):
    pass
class Mutation(videojuegos.schema.Mutation, graphene.ObjectType):
    pass
 
schema = graphene.Schema(query=Query,mutation=Mutation)
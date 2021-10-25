import graphene

import videojuegos.schema


class Query(videojuegos.schema.Query, graphene.ObjectType):
    # Esta clase heredara de multiples consultas
    # segun vayamos agregando aplicaciones a nuestro proyecto
    pass

schema = graphene.Schema(query=Query)

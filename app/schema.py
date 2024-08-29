import graphene
import basic_auth.schema
import basic_auth.schemas.current
import content.schema
import comment.schema
import like.schema


class Query(basic_auth.schema.Query,
            basic_auth.schemas.current.Query,
            content.schema.Query,
            comment.schema.Query,
            like.schema.Query,
            graphene.ObjectType):
    # Combine the queries from different apps
    pass


class Mutation(basic_auth.schemas.current.Mutation,
                content.schema.Mutation,
                comment.schema.Mutation,
                like.schema.Mutation,
                graphene.ObjectType):
    # Combine the mutations from different apps
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
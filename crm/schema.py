import graphene

# Define your GraphQL schema here

class Mutation(graphene.ObjectType):
    # Define mutations like update_low_stock_products here
    pass

class Query(graphene.ObjectType):
    # Define queries here
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

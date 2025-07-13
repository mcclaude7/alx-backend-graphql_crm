import graphene
from graphene_django import DjangoObjectType
from .models import Product
from datetime import datetime

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "stock")

class UpdateLowStockProducts(graphene.Mutation):
    class Arguments:
        pass

    updated_products = graphene.List(ProductType)
    message = graphene.String()

    def mutate(self, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        updated_list = []

        for product in low_stock_products:
            product.stock += 10  # Simulate restocking
            product.save()
            updated_list.append(product)

        return UpdateLowStockProducts(
            updated_products=updated_list,
            message=f"Updated {len(updated_list)} products at {datetime.now().isoformat()}"
        )

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

class Query(graphene.ObjectType):
    # your existing queries
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

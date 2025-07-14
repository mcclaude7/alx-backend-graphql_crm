import graphene
from .models import Product


class ProductType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    stock = graphene.Int()

class UpdateLowStockProducts(graphene.Mutation):
    success = graphene.Boolean()
    message = graphene.String()
    updated_products = graphene.List(graphene.String)

    def mutate(self, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        updated_names = []

        for product in low_stock_products:
            product.stock += 10
            product.save()
            updated_names.append(product.name)

        return UpdateLowStockProducts(
            success=True,
            message=f"{len(updated_names)} products updated",
            updated_products=updated_names
        )

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

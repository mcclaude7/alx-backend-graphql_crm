import graphene
from graphene_django.types import DjangoObjectType
from .models import Product  # assuming a Product model exists

class ProductType(DjangoObjectType):
    class Meta:
        model = Product

class UpdateLowStockProducts(graphene.Mutation):
    class Arguments:
        pass  # no input arguments

    success = graphene.Boolean()
    message = graphene.String()
    updated_products = graphene.List(ProductType)

    def mutate(self, info):
        updated = []
        low_stock_products = Product.objects.filter(stock__lt=10)

        for product in low_stock_products:
            product.stock += 10
            product.save()
            updated.append(product)

        return UpdateLowStockProducts(
            success=True,
            message=f"{len(updated)} product(s) updated.",
            updated_products=updated
        )

class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

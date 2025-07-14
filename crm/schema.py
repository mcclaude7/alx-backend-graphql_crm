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
        updated = []
        low_stock_products = Product.objects.filter(stock__lt=10)
        for product in low_stock_products:
            product.stock += 10
            product.save()
            updated.append(f"{product.name} (Stock: {product.stock})")

        message = "Stock updated for low-stock products."
        return UpdateLowStockProducts(success=True, message=message, updated_products=updated)


class Mutation(graphene.ObjectType):
    update_low_stock_products = UpdateLowStockProducts.Field()

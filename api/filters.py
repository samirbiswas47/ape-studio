import django_filters
from api.models import Product, Order, OrderItem
class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        #fields = ['name', 'price']
        fields = {
            'name':['iexact', 'icontains'],
            'price':['exact', 'gt', 'lt', 'range']
        }
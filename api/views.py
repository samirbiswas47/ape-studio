from django.db.models import Max
#from django.http import JsonResponse
from api.serializers import ProductSerializer, OrderSerializer, ProductInfoSerialization
from api.models import Product, Order, OrderItem
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    AllowAny
)
from rest_framework.views import APIView


#Class base view
class ProductListAPIView(generics.ListAPIView):
    #queryset = Product.objects.filter(stock__gt=0)
    #queryset = Product.objects.exclude(stock__gt=0)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes= [AllowAny]

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method == 'POST':
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()

class ProductGetCreateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg= 'product_id'
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes=[IsAdminUser]
        return super().get_permissions()
class ProductCreateAPIView(generics.CreateAPIView):
    model= Product
    serializer_class = ProductSerializer
    permission_classes= [IsAdminUser]

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg= 'product_id'

class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes= [IsAdminUser]

class UserOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user= self.request.user)

class ProductInfoApiView(APIView):
    def get(self, response):
        products = Product.objects.all()
        serializer = ProductInfoSerialization({
            'products':products,
            'count': len(products),
            'max_price': products.aggregate(max_price = Max('price'))['max_price']
        })
        return Response(serializer.data)


'''
##****** For Json object *************##
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({
        'data':serializer.data
    })

##****** Function base view *************##
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.prefetch_related('items__product')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerialization({
        'products':products,
        'count': len(products),
        'max_price': products.aggregate(max_price = Max('price'))['max_price']
    })
    return Response(serializer.data)
'''

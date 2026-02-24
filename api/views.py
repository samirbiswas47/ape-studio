from django.db.models import Max
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.filters import InStockFilterBackend, OrderFilter, ProductFilter
from api.models import Order, OrderItem, Product, User
#from django.http import JsonResponse
from api.serializers import (OrderSerializer, ProductInfoSerialization,
                             ProductSerializer, OrderCreateSerializer, UserSerializer)

class UserListAPIView(generics.ListAPIView):
    #queryset = Product.objects.filter(stock__gt=0)
    #queryset = Product.objects.exclude(stock__gt=0)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class=None
    permission_classes= [AllowAny]
#Class base view
class ProductListAPIView(generics.ListAPIView):
    #queryset = Product.objects.filter(stock__gt=0)
    #queryset = Product.objects.exclude(stock__gt=0)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes= [AllowAny]
    

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer
    #filterset_fields =('name', 'price')
    filterset_class = ProductFilter
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter, 
        filters.OrderingFilter,
        InStockFilterBackend,
    ]
    search_fields = ['=name','description']
    ordering_fields = ['name', 'price', 'stock']
    class CustomPageNumberPagination(PageNumberPagination):
        page_size = 5
        page_query_param = 'pagenum'
        page_size_query_param = 'size'
        max_page_size = 6

    pagination_class = CustomPageNumberPagination

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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    #permission_classes= [AllowAny]
    permission_classes= [IsAuthenticated]
    pagination_class=None
    filterset_class = OrderFilter
    filter_backends= [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

    def get_serializer_class(self):
        # can also check if POST: if self.request.method == 'POST'
        if self.action == 'create' or self.action == 'update':
            return OrderCreateSerializer
        return super().get_serializer_class()
    
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs= qs.filter(user = self.request.user)
        return qs
    
    # to make additional url request use @action
    @action(
        detail=False, 
        methods=['get'], 
        url_path='userorders',
        #permission_classes=[IsAuthenticated]
    )
    def user_order(self, request):
        orders = self.get_queryset().filter(user= request.user)
        serializer = self.get_serializer(orders, many = True)
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

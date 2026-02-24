from rest_framework import serializers
from .models import Product, Order, OrderItem, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =(
            'id',
            'username',
            'email',
            'is_staff',
            'is_authenticated',
            'get_full_name',
            'orders'
        )
        
        '''
        exclude = ('password', 'user_permissions')
        fields ='__all__'
        '''
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields= (
            'name',
            'price',
            'stock',
            'description',
        ) 
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )
        return value

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    product_name = serializers.CharField(source = 'product.name')
    product_price = serializers.DecimalField(source = 'product.price', max_digits=10, decimal_places=2)
    class Meta:
        model =OrderItem
        fields =(
            'product',
            'product_name',
            'product_price',
            'quantity',
            'item_subtotal'
        )

class OrderCreateSerializer(serializers.ModelSerializer):
    class OrderItemCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderItem
            fields = ('product', 'quantity')
    order_id = serializers.UUIDField(read_only= True)
    items =OrderItemCreateSerializer(many= True)

    def update(self, instance, validated_data):
        orderitem_data = validated_data.pop('items')
        instance = super().update(instance, validated_data)

        if orderitem_data is not None:
            # Clear existing item (optional, depends on requirements)
            instance.items.all().delete()

            # Recreate items with the updated data
            for item in orderitem_data:
                OrderItem.objects.create( order= instance, **item)

            return instance
    
    def create(self, validated_data):
        orderitem_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in orderitem_data:
            OrderItem.objects.create( order= order, **item)

        return order

    class Meta:
        model = Order
        fields =(
            'order_id',
            'user',
            'status',
            'items'
        )
        extra_kwargs = {
            'user': { 'read_only': True }
        }

class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.UUIDField(read_only= True)
    items = OrderItemSerializer(many=True, read_only= True)
    total_price = serializers.SerializerMethodField(method_name="total")

    ## If you not define method_name ##
    # def get_total_price(self, obj):
    #     order_items =obj.items.all()
    #     return sum(order_item.item_subtotal for order_item in order_items)

    def total(self, obj):
        order_items =obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)
    
    class Meta:
        model = Order
        fields =(
            'order_id',
            'created_at',
            'user',
            'status',
            'items',
            'total_price',
        )

class ProductInfoSerialization(serializers.Serializer):
    products= ProductSerializer(many= True)
    count = serializers.IntegerField()
    max_price = serializers.FloatField()
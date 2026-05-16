from rest_framework import serializers
from .models import  User, Portfolio, Service, Testimonial, Enquiry, NewsletterSubscriber

class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(
        source='get_full_name',
        read_only=True
    )
    # Accept raw password input
    password = serializers.CharField(
        write_only=True,
        required=False
    )
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_staff',
            'full_name',
            'password'
        )

    # CREATE USER
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    # UPDATE USER
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        # Encrypt updated password
        if password:
            instance.set_password(password)
        instance.save()
        return instance
        '''
        exclude = ('password', 'user_permissions')
        fields ='__all__'
        '''
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields =(
            'id',
            'title',
            'description',
            'image',
            'project_url',
            'technologies',
            'featured',
            'is_deleted', 
            'is_active',
            'created_at',
            'updated_at'
        )

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields =(
            'id',
            'title',
            'description',
            'icon',
            'is_deleted', 
            'is_active',
            'created_at',
            'updated_at'
        )

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields =(
            'id',
            'client_name',
            'company',
            'feedback',
            'rating',
            'image',
            'is_published',
            'is_deleted', 
            'is_active',
            'created_at',
            'updated_at'
        )
class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields =(
            'id',
            'name',
            'email',
            'phone',
            'service_interest',
            'message',
            'is_read',
            'is_deleted', 
            'is_active',
            'created_at',
            'updated_at'
        )

class NewsletterSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscriber
        fields =(
            'id',
            'email',
            'subscribed_at',
            'is_deleted', 
            'is_active',
            'created_at',
            'updated_at'
        )
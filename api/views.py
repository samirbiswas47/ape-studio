from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import filters, generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


from api.models import  User, Portfolio, Service, Testimonial, Enquiry, NewsletterSubscriber
from api.filters import PortfolioFilter, ServiceFilter, TestimonialFilter, UserFilter, EnquiryFilter, NewsletterSubscriberFilter
from api.serializers import ( UserSerializer, PortfolioSerializer, ServiceSerializer, TestimonialSerializer, EnquirySerializer, NewsletterSubscriberSerializer)

User = get_user_model()


# class UserListAPIView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     pagination_class=None
#     permission_classes= [AllowAny]
#     permission_classes= [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class=None
    filterset_class = UserFilter
    filter_backends= [DjangoFilterBackend]    
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes=[IsAuthenticated]
        return super().get_permissions()

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    pagination_class=None
    filterset_class = PortfolioFilter
    filter_backends= [DjangoFilterBackend]
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes=[IsAuthenticated]
        return super().get_permissions()

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class=None
    filterset_class = ServiceFilter
    filter_backends= [DjangoFilterBackend]
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes=[IsAuthenticated]
        return super().get_permissions()

class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    pagination_class=None
    filterset_class = TestimonialFilter
    filter_backends= [DjangoFilterBackend]
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes=[IsAuthenticated]
        return super().get_permissions()
    
class EnquiryViewSet(viewsets.ModelViewSet):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    pagination_class=None
    filterset_class = EnquiryFilter
    filter_backends= [DjangoFilterBackend]
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes=[IsAuthenticated]
        return super().get_permissions()
    
class NewsletterSubscriberViewSet(viewsets.ModelViewSet):
    queryset = NewsletterSubscriber.objects.all()
    serializer_class = NewsletterSubscriberSerializer
    pagination_class=None
    filterset_class = NewsletterSubscriberFilter
    filter_backends= [DjangoFilterBackend]
    def get_permissions(self):
        self.permission_classes=[AllowAny]
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes=[IsAuthenticated]
        return super().get_permissions()
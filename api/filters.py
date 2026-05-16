import django_filters
from api.models import User, Portfolio, Service, Testimonial, Enquiry, NewsletterSubscriber
from rest_framework import filters

class PortfolioFilter(django_filters.FilterSet):
    #created_at = django_filters.DateFilter('created_at__date')
    class Meta:
        model = Portfolio
        fields = ['title']

class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Service
        fields = ['title']

class TestimonialFilter(django_filters.FilterSet):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'rating']

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]

class EnquiryFilter(django_filters.FilterSet):
    class Meta:
        model = Enquiry
        fields = [
            'name',
            'email',
            'phone',
            'service_interest',
            'is_read',
        ]


class NewsletterSubscriberFilter(django_filters.FilterSet):
    class Meta:
        model = NewsletterSubscriber
        fields = [
            'email',
            'subscribed_at',
        ]
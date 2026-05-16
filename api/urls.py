from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    #path('users/', views.UserListAPIView.as_view()),
]

router = DefaultRouter()
router.register('portfolio', views.PortfolioViewSet)
router.register('services', views.ServiceViewSet)
router.register('testimonials', views.TestimonialViewSet)
router.register('users', views.UserViewSet)
router.register('enquiries', views.EnquiryViewSet)
router.register('newsletter-subscriber', views.NewsletterSubscriberViewSet)
urlpatterns += router.urls

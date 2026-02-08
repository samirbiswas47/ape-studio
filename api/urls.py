from django.urls import path
from . import views

urlpatterns = [
    # path('products/', views.product_list),
    #path('product/<int:id>', views.product_detail),
    #path('orders/', views.order_list),
    #path('products/info', views.product_info),
    path('products/', views.ProductListAPIView.as_view()),
    path('products/create', views.ProductCreateAPIView.as_view()),
    path('products/<int:product_id>', views.ProductDetailAPIView.as_view()),
    path('orders/', views.OrderListAPIView.as_view()),
    path('user-orders/', views.UserOrderListAPIView.as_view(), name='user-orders'),
    path('products/info', views.ProductInfoApiView.as_view()),
]

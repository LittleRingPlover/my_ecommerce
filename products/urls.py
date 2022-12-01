from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.show_all_products, name='show_products'),
    path('product/<int:pk>/', views.product_detail, name='product_detail')
]
from django.urls import path
from rest_api.views import ProductDetailView, ProductListView, CreateProductView, UpdateProductView, DeleteProductView

app_name = 'rest_api'
urlpatterns = [
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create', CreateProductView.as_view(), name='new_product'),
    path('products/<int:pk>/update', UpdateProductView.as_view(), name='update_product'),
    path('products/<int:pk>/delete', DeleteProductView.as_view(), name='delete_product'),
]

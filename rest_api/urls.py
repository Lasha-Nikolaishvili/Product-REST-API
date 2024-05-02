from django.urls import path
from rest_api.views import ProductDetailView, ProductListView, CreateProductView, UpdateProductView, DeleteProductView

app_name = 'rest_api'
urlpatterns = [
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_details'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('new-product/', CreateProductView.as_view(), name='new_product'),
    path('update-product/<int:pk>', UpdateProductView.as_view(), name='update_product'),
    path('delete-product/<int:pk>', DeleteProductView.as_view(), name='delete_product'),
]

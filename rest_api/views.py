from rest_framework.viewsets import ModelViewSet
from rest_api.serializers import (
    ProductSerializer, ProductListSerializer, ProductUpdateSerializer, ProductCategorySerializer
)
from rest_api.permissions import IsAdminOrReadOnly
from rest_api.paginations import ProductPagination
from rest_api.utils import SerializerFactory
from store.models import Product, ProductCategory


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    pagination_class = ProductPagination
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = SerializerFactory(
        default=ProductSerializer,
        list=ProductListSerializer,
        update=ProductUpdateSerializer,
        partial_update=ProductUpdateSerializer,
    )


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAdminOrReadOnly]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_api.views import ProductViewSet, ProductCategoryViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', ProductCategoryViewSet, basename='category')

app_name = 'rest_api'
urlpatterns = [
    path('', include(router.urls))
]

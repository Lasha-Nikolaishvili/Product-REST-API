from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from store.models import Product, ProductCategory


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['stock']


class ProductCategorySerializer(ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = '__all__'

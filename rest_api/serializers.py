from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from store.choices import Category
from store.models import Product, ProductCategory


class ProductSerializer(ModelSerializer):
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        return [Category(category).label for category in obj.categories.all().values_list('category', flat=True)]

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'categories']


class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'category']


class CreateProductSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all(), many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'categories']

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        product = Product.objects.create(**validated_data)
        for category_data in categories_data:
            product.categories.add(category_data)
        return product


class ProductUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['stock']

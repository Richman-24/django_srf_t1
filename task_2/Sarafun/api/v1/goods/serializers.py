from rest_framework import serializers

from goods.models import Category, SubCategory, Product


class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ('name', 'slug', 'image')


class CategorySerializer(serializers.ModelSerializer):

    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('name', 'slug', 'image', 'subcategories')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'name',
            'slug',
            'small_img',
            'medium_img',
            'large_img',
            'price',
            'sub_category'
        )
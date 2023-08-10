from rest_framework import serializers
from apps.products.models import MeasureUnit, Category, Discount

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('status',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('status',)


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ('status',)
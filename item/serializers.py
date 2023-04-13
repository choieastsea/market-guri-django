from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__" # 아이템의 모든 필드를 serialize해줄 것임

    def validate_price(self, value):
        if value == 0:
            raise serializers.ValidationError("price must be positive") 
        return value

# class ItemSerializer(serializers.Serializer):
#     item_id = serializers.IntegerField(label='상품코드', read_only=True)
#     name = serializers.CharField(label='상품명', max_length=100)
#     price = serializers.IntegerField(label='상품가격', max_value=4294967295, min_value=0)
#     stock_count = serializers.IntegerField(label='남은수량', max_value=4294967295, min_value=0)
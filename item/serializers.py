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

class ItemCartSerializer(serializers.ModelSerializer):
    """
    Cart에 들어가는 Item을 위한 serializer (item_id를 제외하고는 read_only로!)
    """
    item_id = serializers.IntegerField()
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ('name', 'price', 'stock_count', 'description')
    
# class ItemSerializer(serializers.Serializer):
#     item_id = serializers.IntegerField(label='상품코드', read_only=True)
#     name = serializers.CharField(label='상품명', max_length=100)
#     price = serializers.IntegerField(label='상품가격', max_value=4294967295, min_value=0)
#     stock_count = serializers.IntegerField(label='남은수량', max_value=4294967295, min_value=0)
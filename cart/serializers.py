from rest_framework import serializers
from .models import Cart
from item.serializers import ItemCartSerializer

class CartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only= True)
    total_price = serializers.SerializerMethodField()
    is_available_now = serializers.SerializerMethodField(method_name='is_available')

    def get_total_price(self, obj):
        # 총 금액 리턴
        return obj.item.price * obj.amount
    
    def is_available(self, obj):
        # 현재 수량이 주문 가능한지
        return obj.item.stock_count >= obj.amount
    
    def create(self, validated_data):
        # user, itm_info 이미 존재한다면 수량만 누적하는 update
        cart_exist = Cart.objects.filter(user=validated_data.get('user'), item=validated_data.get('item')).first()
        if cart_exist:
            validated_data['amount'] = validated_data.get('amount') + cart_exist.amount
            return self.update(cart_exist, validated_data)
        # 존재하지 않는다면 create
        else:
            return super().create(validated_data)
    
    # item을 보여줄 때, id만 보여주는 것이 아닌, 안의 내용들을 ItemCartSerializer 통해서 보여주도록 해야함
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['item'] = ItemCartSerializer(instance.item).data
        return response
    
    class Meta:
        model = Cart
        fields = "__all__"
        

class CartUpdateSerializer(serializers.ModelSerializer):
    item = ItemCartSerializer(read_only=True) # 아이템 정보 보여주기 read_only

    class Meta:
        model = Cart
        fields = ('amount', 'item',)
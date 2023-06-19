from rest_framework import viewsets
from .serializers import CartSerializer, CartUpdateSerializer
from .models import Cart
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CartModelViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated] # 인증된 사용자만 접근 가능
    
    def get_queryset(self):
        # 본인이 장바구니에 포함시킨 것들만 보여주도록 해야함(타인 접근 불가)
        queryset = Cart.objects.filter(user=self.request.user)
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'update':
            return CartUpdateSerializer
        else:
            return CartSerializer

    def perform_create(self, serializer):
        # cart 생성되기 전, serializer에 auth에 해당하는 user 정보 넣어줘야함
        serializer.save(user=self.request.user)
    
    # def update(self, request, *args, **kwargs):
    #     # print(kwargs) # pk
    #     # origin_obj = Cart.objects.get(id=kwargs['pk'])
    #     # print(request.data) #body
    #     # request.data['item'] = [origin_obj.item]
    #     kwargs['partial'] = True # for partial update
    #     return super().update(request, *args, **kwargs)


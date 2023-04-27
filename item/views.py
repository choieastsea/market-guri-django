from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer


# ModelViewSet 이용한 CBV
class ItemModelViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet을 이용하여 item의 모든 기능을 제공하는 클래스
    queryset, serializer_class만 정의하면 다양한 패턴에 대하여 구현 가능
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        name = self.request.query_params.get('name')
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset
    
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True # for partial update
        return super().update(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        # print(request.META['HTTP_ORIGIN']) # CORS error가 발생하더라도 view가 실행됨
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        print('create') # CORS error가 발생하더라도 view가 실행됨
        return super().create(request, *args, **kwargs)

@api_view(['GET'])
def index(request):
    # serialize
    items = Item.objects.all() # return QuerySet(not yet query)
    # print(items)
    itemSerializer = ItemSerializer(items, many=True) # return OrderedDict
    # print(itemSerializer)
    # print(itemSerializer.data)
    return Response(itemSerializer.data)

@api_view(['POST'])
def create_item(request):
    itemSerializer = ItemSerializer(data=request.data)
    if itemSerializer.is_valid():
        itemSerializer.save()
        return Response(itemSerializer.data)
    return Response(itemSerializer.errors) # error occured

class ItemListView(APIView):
    """
    item list를 리턴하거나 새로운 item을 create하는 클래스
    """
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       

class ItemDetailView(APIView):
    """
    특정 pk의 Item을 Read, Update, Delete하는 클래스
    요청에 대하여 pk가 주어져야 한다
    """
    def get_object(self, pk):
        # 특정 pk의 Item을 리턴
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            # Item이 없다면 DoesNotExist error throw
            # 이에 404오류를 발생시키도록 한다
            raise Http404
        
    def get(self, request, pk):
        item = self.get_object(pk) # error 발생하면 이후 실행되지 않고 바로 404 response
        serializer = ItemSerializer(item) # 직렬화(DB to json) 수행, 하나이므로 many=True일 필요없음
        return Response(serializer.data)
    
    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data, partial=True) # serailizer의 update 함수 수행, partial fields 업데이트 허용
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()   # pk 기반의 삭제는 serializer를 사용하지 않고 ORM의 delete를 수행한다
        return Response(status=status.HTTP_204_NO_CONTENT)


# GenericAPIView + mixins 이용한 CBV
class ItemListGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """
    GenericAPIView를 이용하여 item의 리스트를 얻도록 하는 클래스
    queryset과 serailizer_class 정의해줘야함.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request): # get override
        return self.list(request) # from mixins.ListModelMixin
    
    def post(self, request): # post override
        return self.create(request) # from mixins.CreateModelMixin

class ItemDetailGenericAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get(self, request, *args, **kargs):
        return self.retrieve(self, request, *args, **kargs) # from mixins.RetrieveModelMixin

    def put(self, request, *args, **kargs): # update override
        return self.update(request, *args, **kargs) # from mixins.UpdateModelMixin
    
    def delete(self, request, *args, **kargs): # delete override
        return self.destroy(request, *args, **kargs) # from mixins.DestroyModelMixin

# Generic 이용한 CBV
class ItemDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    """
    GenericView를 이용하여 item의 특정정보를 얻거나, 업데이트, 삭제 하도록 하는 클래스 
    queryset, serializer_class를 정의해야함
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemListGenericView(generics.ListCreateAPIView):
    """
    GenericView를 이용하여 item의 list얻거나 create 하도록 하는 클래스 
    queryset, serializer_class를 정의해야함
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

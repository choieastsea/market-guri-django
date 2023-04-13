from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer

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

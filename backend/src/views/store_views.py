from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from src.models import *
from src.serializer import *


@api_view(['GET'])
def getStores(request):
    queryset=stores.objects.all()
    serializer=StoreSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStoreOwners(request):
    owners=store_owner.objects.all()
    serializer=StoreOwner_Serializer(owners,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStoreById(request,pk):
    stores=stores.object.get(_id=pk)
    serializer=StoreSerializer(stores,many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getStoreOwnerById(request,pk):
    store_owner=store_owner.objects.get(_id=pk)
    serializers=StoreOwner_Serializer(store_owner,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def createStoreBrand(request,pk):
    store=stores.objects.get(_id=pk)
    data = request.data
    Brand=brand.object.create(
        name=data['name'],
        quantity=data['quantity'],
        status=data['status']
    )

    brands=stores.brand_set.all()
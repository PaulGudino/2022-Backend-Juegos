from AppJuegos.models import (
    Publicity,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Publicity.PublicitySerializers import (
    PublicitySerializers,
    # PublicitySerializerCreate,
    # PublicitySerializerUpdate
)

from rest_framework import status
from rest_framework.response import Response

class PublicityViewSet(CRUDViewSet):
    serializer_class = PublicitySerializers
    queryset = Publicity.objects.all()

    # def create(self, request):
    #     serializer = PublicitySerializerCreate(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def update(self, request, pk):
    #     print('update publicity beggin')
    #     publicity = Publicity.objects.get(id=pk)
    #     print("request de publicity")
    #     print(request.data.get('id'))
        
    #     #new_start_date = request.data.get('start_date')

    #     serializer = PublicitySerializerUpdate(publicity, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


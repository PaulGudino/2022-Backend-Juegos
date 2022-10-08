from email.mime import image
import os
from AppJuegos.models import (
    Premios,
    # User
)
# from rest_framework.generics import GenericAPIView
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Premios.PremiosSerializers import (
    PremiosSerializer,
    PremiosSerializerCreate,
    PremiosSerializerUpdateImage,
    PremiosSerializerUpdateSinImage,
)
from rest_framework import status
from rest_framework.response import Response


class PremiosViewSet(CRUDViewSet):
    serializer_class = PremiosSerializer
    queryset = Premios.objects.all()

    def create(self, request):
        serializer = PremiosSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        premio = Premios.objects.get(id=pk)
        new_image = request.data.get('image')
        if new_image:
            serializer = PremiosSerializerUpdateImage(premio, data=request.data)
            if serializer.is_valid():
                old_image = premio.image
                os.remove(old_image.path)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = PremiosSerializerUpdateSinImage(premio, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







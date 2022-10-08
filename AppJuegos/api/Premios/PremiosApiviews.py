from email.mime import image
from AppJuegos.models import (
    Premios,
    # User
)
# from rest_framework.generics import GenericAPIView
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Premios.PremiosSerializers import (
    PremiosSerializer,
    PremiosSerializerCreate,
    PremiosSerializerUpdate,
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
        model = self.get_serializer().Meta.model
        instance = model.objects.get(pk=pk)
        serializer = PremiosSerializerUpdate(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





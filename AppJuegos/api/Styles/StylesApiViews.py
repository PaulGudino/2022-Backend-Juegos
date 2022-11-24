from AppJuegos.models import (
    Styles,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Styles.StylesSerializers import (
    StylesSerializers,
    
)

from rest_framework import status
from rest_framework.response import Response

class StylesViewSet(CRUDViewSet):
    serializer_class = StylesSerializers
    queryset = Styles.objects.all()

    def create(self, request):
        serializer = StylesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        style = Styles.objects.get(id=pk)
        print(request.data.get('id'))
        print(style)
        #new_start_date = request.data.get('start_date')

        serializer = StylesSerializers(style, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




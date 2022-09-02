from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


# Solo GET
class GeneralListApiView(generics.ListAPIView):
    serializer_class = None

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.all()

# GET Y POST
class GeneralListCreateApiView(generics.ListCreateAPIView):
    serializer_class = None
    queryset = None

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# GET, PUT y DELETE
class GeneralRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = None

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(pk=pk).first()

    def put(self, request, pk, format=None):
        model = self.get_serializer().Meta.model
        instance = model.objects.get(pk=pk)
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        model = self.get_serializer().Meta.model
        model.objects.get(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
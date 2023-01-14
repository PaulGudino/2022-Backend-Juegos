from AppJuegos.models import (
    Audio,
)
import os
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Audio.AudioSerializers import (
    AudioSerializers,
)

from rest_framework import status
from rest_framework.response import Response

class AudioViewSet(CRUDViewSet):
    serializer_class = AudioSerializers
    queryset = Audio.objects.all()

    def create(self, request):
        serializer = AudioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        audio = Audio.objects.get(id=pk)

        new_audio = request.data.get('audio')

        serializer = AudioSerializers(audio, data=request.data)
        if serializer.is_valid():
            if new_audio:
                old_audio = audio.audio
                if old_audio:
                    os.remove(old_audio.path)

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


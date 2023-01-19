from AppJuegos.models import (
    Styles,
)
import os
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

        new_image_machine_game = request.data.get('image_machine_game')
        new_image_background_game = request.data.get('image_background_game')
        new_image_logo_game = request.data.get('image_logo_game')
        new_video_screensaver = request.data.get('video_screensaver')
        new_image_winner = request.data.get('image_winner')

        serializer = StylesSerializers(style, data=request.data)
        if serializer.is_valid():
            if new_image_machine_game:
                old_image_machine_game = style.image_machine_game
                if old_image_machine_game:
                    os.remove(old_image_machine_game.path)

            if new_image_background_game:
                old_image_background_game = style.image_background_game
                if old_image_background_game:
                        os.remove(old_image_background_game.path)
            
            if new_image_logo_game:
                old_image_logo_game = style.image_logo_game
                if old_image_logo_game:
                        os.remove(old_image_logo_game.path)

            if new_video_screensaver:
                old_video_screensaver = style.video_screensaver
                if old_video_screensaver:
                        os.remove(old_video_screensaver.path)
            
            if new_image_winner:
                old_image_winner = style.image_winner
                if old_image_winner:
                        os.remove(old_image_winner.path)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




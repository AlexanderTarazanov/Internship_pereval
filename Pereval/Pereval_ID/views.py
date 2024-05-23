from rest_framework import viewsets, status
from .serializers import *
from .models import *
from rest_framework.response import Response
import django_filters


class UserViewset(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['fam', 'name', 'otc', 'email']


class CoordsViewset(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class LevelViewset(viewsets.ModelViewSet):
   queryset = Level.objects.all()
   serializer_class = LevelSerializer


class ImageViewset(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer


class PerevalViewset(viewsets.ModelViewSet):
    queryset = pereval_added.objects.all()
    serializer_class = PerevalSerializer
    filterset_fields = ('tourist_id__email',)

    def create(self, request, *args, **kwargs):
        if self.action == 'create':
            serializer = PerevalSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': status.HTTP_200_OK,
                        'message': 'Успех!',
                        'id': serializer.instance.pk,
                    }
                )

            if status.HTTP_400_BAD_REQUEST:
                return Response(
                    {
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'Bad Request',
                        'id': None,
                    }
                )

            if status.HTTP_500_INTERNAL_SERVER_ERROR:
                return Response(
                    {
                        'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
                        'message': 'Ошибка подключения к базе данных',
                        'id': None,
                    }
                )
        return super().create(request, *args, **kwargs)


    def update(self, instance, validated_data):
        tourist_id = validated_data.pop('tourist_id')
        coord_id = validated_data.pop('coord_id')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        tourist_id = Users.objects.update(**tourist_id)
        coord_id = Coords.objects.update(**coord_id)
        level = Level.objects.update(**level)

        for i in images:
            image = i.pop('image')
            title = i.pop('title')
            Images.objects.create(image=image, title=title)

        return super().update(instance, validated_data)
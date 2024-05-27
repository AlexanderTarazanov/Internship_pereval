from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email', 'fam', 'name', 'otc', 'phone',)


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'spring', 'summer', 'autumn',)


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.URLField()

    class Meta:
        model = Images
        fields = ('image', 'title',)


class PerevalSerializer(WritableNestedModelSerializer):
    add_time = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', read_only=True)
    tourist_id = UserSerializer()
    coord_id = CoordsSerializer()
    level = LevelSerializer(allow_null=True)
    images = ImageSerializer(many=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = pereval_added
        depth = 1
        fields = (
            'id',
            'status',
            'tourist_id',
            'add_time',
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'coord_id',
            'level',
            'images',
        )

    def create(self, validated_data, **kwargs):
        tourist_id = validated_data.pop('tourist_id')
        coord_id = validated_data.pop('coord_id')
        level = validated_data.pop('level')
        images = validated_data.pop('images')

        tourist_id, created = Users.objects.get_or_create(**tourist_id)

        coord_id = Coords.objects.create(**coord_id)
        level = Level.objects.create(**level)
        pereval = pereval_added.objects.create(**validated_data, tourist_id=tourist_id, coord_id=coord_id,
                                               level=level, status='new')

        for i in images:
            image = i.pop('image')
            title = i.pop('title')
            Images.objects.create(image=image, pereval_id=pereval, title=title)

        return pereval

    def validate(self, data):
        if self.instance is not None:
            instance_tourist_id = self.instance.tourist_id
            data_tourist_id = data.get('tourist_id')
            validating_tourist_id_fields = [
                instance_tourist_id.fam != data_tourist_id['fam'],
                instance_tourist_id.name != data_tourist_id['name'],
                instance_tourist_id.otc != data_tourist_id['otc'],
                instance_tourist_id.phone != data_tourist_id['phone'],
                instance_tourist_id.email != data_tourist_id['email'],
            ]
            if data_tourist_id is not None and any(validating_tourist_id_fields):
                raise serializers.ValidationError({'Отклонено': 'Нельзя изменять данные пользователя'})
        return data
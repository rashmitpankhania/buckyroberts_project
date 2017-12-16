from rest_framework import serializers
from .models import Album,Song

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fiels = ['albumn_title']


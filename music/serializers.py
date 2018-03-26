import django.rest_framework
from .models import Album,Song

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fiels = ['albumn_title']


from media_file.models import SimpleFile
from rest_framework import serializers


class SimpleFileSerializer(serializers.HyperlinkedModelSerializer):
    image_url = serializers.FileField(use_url=True)



    class Meta:
        model = SimpleFile
        fields = '__all__'


from rest_framework import serializers
from Todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

    class Meta:
        model = Todo
        fields = "__all__"

from rest_framework import serializers    
from deepopinion_backend_challenge.data_app.models import Tag, Data


class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ("id", "aspect", "sentiment")

class DataSerializer(serializers.ModelSerializer):
    # This line is what changed:
    tags = TagSerializer(many=True)

    class Meta:
        model = Data
        fields = ("id", "text", "tags")

    def create(self, validated_data):
        # create product
        tags_data = validated_data.pop('tags')
        data = Data.objects.create(**validated_data)
        #user = self.context['request'].user
        for tag_data in tags_data:
            new_data_tags = Tag.objects.create(data=data, tags=tag_data)
        return data
    
    class Meta:
        model = Data
        lookup_field = 'id'
        fields = [
                    'id',
                    'text',
                    'tags',
                ]

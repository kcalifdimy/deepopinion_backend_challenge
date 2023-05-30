import pandas as pd
from rest_framework import serializers    
from deepopinion_backend_challenge.data_app.models import Text, Tag
# from deepopinion_backend_challenge.data_app.models.tags import Tag



class FileUploadSerializer(serializers.Serializer):
    """
    Created a Serializer to upload files
    """
    file_upload = serializers.FileField()


class TagSerializer(serializers.ModelSerializer):
    """
    Created a Serializer for tag features
    """
    class Meta:
        model = Tag
        fields = ("id", "aspect", "sentiment")



class DataSerializer(serializers.ModelSerializer):
    """
    Created a Dataserializer that helps to display all datas and tags
    """
    

    tags = TagSerializer(many=True)

    # This function create data with it respective tags
    def create(self, validated_data):
        tags_data = validated_data.pop('tags')
        data = Text.objects.create(**validated_data) 
        for tag_data in tags_data:
            new_data_tags = Tag.objects.create(data=data, tags=tag_data)
        return data
    
    # This function change/add tags to data 
    def update(self, instance, validated_data):
        tag_data = validated_data.pop('tags')
        instance = super().update(instance, validated_data)
        instance.save()
        if tag_data:
            data_tags_model_instance = [Tag(text=instance, **tag) for tag in tag_data]
            Tag.objects.bulk_create(data_tags_model_instance)
        return instance


    class Meta:
        model = Text
        lookup_field = 'id'
        fields = [
                    'id',
                    'text',
                    'tags',
                ]

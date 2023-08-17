
from rest_framework import serializers
from notion.models import Notion

class NotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notion
        fields = ('id', 'title', 'content', 'image')
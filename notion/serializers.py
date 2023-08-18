
from rest_framework import serializers
from notion.models import Notion

from notion.models import Product

class NotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notion
        fields = ('id', 'title', 'content', 'image')
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('productId', 'productTitle', 'productContent', 'productImage','productOption')

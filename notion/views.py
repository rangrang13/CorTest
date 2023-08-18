from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from notion.models import Notion
from notion.serializers import NotionSerializer
from .models import Product
from .serializers import ProductSerializer

class NotionViewSet(viewsets.ModelViewSet):
    queryset = Notion.objects.all()
    serializer_class = NotionSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

   




# Create your views here.

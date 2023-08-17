
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from notion.models import Notion
from notion.serializers import NotionSerializer

class NotionViewSet(viewsets.ModelViewSet):
    queryset = Notion.objects.all()
    serializer_class = NotionSerializer
    #permission_classes = [IsAuthenticated] #로그인 한 사람만 글 쓸수 있게함

    #def perform_create(self, serializer):
        #serializer.save(author=self.request.user)




# Create your views here.

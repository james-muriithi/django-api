from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from app.models import News
from app.permissions import IsAdmin
from app.serializer import NewsSerializer

# Create your views here.


def index(request):
    return render(request, 'index.html')


class NewsList(APIView):
    permission_classes = (IsAdmin,)

    def get(self, request):
        news = News.objects.all()
        serializers = NewsSerializer(news, many=True)

        return Response(serializers.data)

    def post(self, request):
        serializers = NewsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=HTTP_201_CREATED)
        return Response(serializers.errors, status=HTTP_400_BAD_REQUEST)


class NewsDescription(APIView):
    def get_news(self, id):
        try:
            return News.objects.get(id=id)
        except News.DoesNotExist:
            return Http404

    def get(self, request, id):
        news = self.get_news(id)
        serializers = NewsSerializer(news)
        return Response(serializers.data)

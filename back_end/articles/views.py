from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Article
from accounts.models import User
from .serializers import ArticleSerializer, ArticleListSerializer, UserArticleSerializer

# Create your views here.

@api_view(['GET'])
def article_list(request):
    article = Article.objects.all()
    serializer = ArticleListSerializer(article, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_article(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def user_article(request, username):
    # 유저 객체를 먼저 불러오고
    user = get_object_or_404(User, username=username)
    # 해당 유저로 필터 -> 아티클 불러오기
    article = Article.objects.filter(user=user)
    serializer = UserArticleSerializer(article, many=True)
    return Response(serializer.data)

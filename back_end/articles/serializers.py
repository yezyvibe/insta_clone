from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.modelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'created_at']

class ArticleSerializer(serializers.modelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

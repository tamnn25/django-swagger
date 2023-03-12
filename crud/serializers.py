from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):

    title = serializers.CharField(error_messages={'blank': 'My customized message for name.'})
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email']
       


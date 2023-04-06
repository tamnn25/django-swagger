from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    description = serializers.CharField(error_messages={'blank': 'My customized message for name.'})
    
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email', 'description']

        
    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        print(data,12121)
        if data['title']:
            raise serializers.ValidationError("hello error mess")
        return data
    
    def validate_description(self, value: str) -> str:
        print(1111, value)
        return "hello" + value

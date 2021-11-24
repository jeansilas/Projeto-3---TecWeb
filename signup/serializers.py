from rest_framework import serializers
from .models import Account, Notes, Tag


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'name','age' ,'date']

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title','content','tag' ,'account']
        
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag']
        
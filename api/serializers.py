from .models import Person
from rest_framework import serializers


class CreateUserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = ('id', 'name',)
        
    
    def create(self, validated_data):
        """Create and return a new Person instance given a validated data"""
        return super().create(validated_data)


class UpdatePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


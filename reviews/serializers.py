from django.contrib.auth.models import User, Group
from .models import Review, Category, Business
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class RegisterUserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password']
        ) 

        return user
    
    class Meta:
        model = User
        fields = ['url', 'username', 'password', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ReviewReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1

class ReviewWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = [
            'url',
            'title',
            'content',
            'stars',
            'business'
        ]

class BusinessReadSerializer(serializers.HyperlinkedModelSerializer):   

    class Meta:
        model = Business
        fields = [
            'url',
            'name',
            'slug',
            'description',
            'price_range',
            'street_address',
            'city',
            'region',
            'postal_code',
            'country',
            'website',
            'phone',
            'hours',
            'reviews',
        ]
        depth = 1

class BusinessWriteSerializer(serializers.HyperlinkedModelSerializer):   

    class Meta:
        model = Business
        fields = [
            'url',
            'name',
            'slug',
            'description',
            'price_range',
            'street_address',
            'city',
            'region',
            'postal_code',
            'country',
            'website',
            'phone',
            'hours',
            'reviews',
        ]

class CategoryReadSerializer(serializers.HyperlinkedModelSerializer):
    business = BusinessReadSerializer(many=True)
    class Meta:
        model = Category
        fields = [
            'url',
            'name',
            'slug',
            'ordinal',
            'business',            
        ]
        depth = 1

class CategoryWriteSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'url',
            'name',
            'slug',
            'ordinal',
            'business',            
        ]
        


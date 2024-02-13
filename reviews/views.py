from django.contrib.auth.models import User, Group
from .models import Review, Category, Business
from .serializers import UserSerializer, GroupSerializer, ReviewSerializer, CategorySerializer, BusinessSerializer
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]    

class BusinessViewset(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['slug']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



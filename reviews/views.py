from django.contrib.auth.models import User, Group
from .models import Review, Category, Business
from .serializers import UserSerializer, GroupSerializer, ReviewReadSerializer, ReviewWriteSerializer, CategoryReadSerializer, CategoryWriteSerializer, BusinessReadSerializer, BusinessWriteSerializer
from rest_framework import viewsets, permissions
from rest_framework.generics import RetrieveAPIView
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
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return ReviewWriteSerializer
        else:
            return ReviewReadSerializer  

class BusinessViewset(viewsets.ModelViewSet):
    queryset = Business.objects.all()    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return BusinessWriteSerializer
        else:
            return BusinessReadSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields =['slug']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return CategoryWriteSerializer
        else:
            return CategoryReadSerializer
        

class UserApiView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



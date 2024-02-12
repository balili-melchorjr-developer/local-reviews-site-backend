from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from reviews import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewset)
router.register(r'groups', views.GroupViewset)
router.register(r'reviews', views.ReviewViewset)
router.register(r'categories', views.CategoryViewset)
router.register(r'businesses', views.BusinessViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

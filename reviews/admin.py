from django.contrib import admin
from .models import Review, Category, Business

# Register your models here.

admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Business)


from django.contrib import admin
from .models import UserProfile, Product, Rating, Comment

admin.site.register(UserProfile)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Comment)

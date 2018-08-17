from django.contrib import admin

# Register your models here.

from .models import Author, Article

admin.site.register(Author)
admin.site.register(Article)

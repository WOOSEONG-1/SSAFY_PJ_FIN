from django.contrib import admin
from .models import Board, Article, Comment
# Register your models here.
admin.site.register(Board)
admin.site.register(Article)
admin.site.register(Comment)
# chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('similar_user/', views.cosine_recommend),
    path('ai_product/', views.recommend_product),
]
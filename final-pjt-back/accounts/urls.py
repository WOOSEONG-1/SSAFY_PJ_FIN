from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:username>/',views.profile_detail ),
    path('logout/',views.logout),
    path('<str:username>/subdeposits/<int:product_id>/', views.subscribe_deposit),
    path('<str:username>/subdeposits/', views.subdeposit_list, ),
    path('<str:username>/subsavings/<int:product_id>/', views.subscribe_saving),
    path('<str:username>/subsavings/', views.subsaving_list ),
]
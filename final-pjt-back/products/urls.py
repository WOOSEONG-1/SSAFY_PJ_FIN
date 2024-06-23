from django.urls import path

from . import views

urlpatterns = [
    path('save-products/',views.save_products ),
    path('deposit_products/',views.deposit_products),
    path('deposit_options/',views.deposit_options),
    path('savings_products/',views.saving_products),
    path('savings_options/',views.saving_options),
    path('deposit_products/<int:pid>/',views.deposit_product_detail),
    path('deposit_options/<int:pid>/',views.deposit_option_detail),
    path('savings_products/<int:pid>/',views.saving_product_detail),
    path('savings_options/<int:pid>/',views.saving_option_detail),
]

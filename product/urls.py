from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('catalog/', views.ProductCatalogView.as_view(), name='product_catalog'),
]

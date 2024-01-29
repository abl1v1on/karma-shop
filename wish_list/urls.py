from django.urls import path

from . import views

app_name = 'wish_list'

urlpatterns = [
    path('<int:pk>/', views.show_user_wish_list, name='user_wish_list'),
    path('add-item/<slug:slug>/', views.add_product_in_wish_List, name='add_item'),
    path('remove-item/<slug:slug>/', views.remove_product_from_wish_list, name='remove_item')
]

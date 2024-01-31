from django.urls import path

from . import views

app_name = 'wish_list'

urlpatterns = [
    path('<int:pk>/', views.show_user_wish_list, name='user_wish_list'),
    path('add-item/<int:pk>/', views.add_to_wish_list, name='add_item'),
    path('remove-item/<int:pk>/', views.remove_from_wish_list, name='remove_item')
]

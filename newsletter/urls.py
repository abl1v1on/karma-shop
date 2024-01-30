from django.urls import path

from . import views

app_name = 'newsletter'


urlpatterns = [
    path('create-new-contact/', views.create_new_contact_view, name='create_new_contact')
]

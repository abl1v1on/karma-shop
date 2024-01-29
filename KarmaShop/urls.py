from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('product/', include('product.urls', namespace='product')),
    path('user/', include('users.urls', namespace='user')),
    path('wish-list/', include('wish_list.urls', namespace='wish_list'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

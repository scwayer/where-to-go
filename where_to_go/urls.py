from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('places/<int:id>/', views.get_place, name='json_response'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

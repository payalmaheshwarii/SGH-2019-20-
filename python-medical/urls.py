import django.contrib
from django.urls import path, include

urlpatterns = [
    path('admin/', django.contrib.admin.site.urls),
    path('', include('home.urls')),
]

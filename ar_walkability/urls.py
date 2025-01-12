from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('guide.urls')),
    path('authentication/', include('user_authentication.urls')),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('auth0authorization.urls')),
    path('admin/', admin.site.urls),
    path('api/cars/', include('cars.urls')),
    path('api/houses/', include('houses.urls')),
    path('api/jobs/', include('jobs.urls'))
]

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from myapp.views import CarViewSet, AnimalViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarViewSet)
router.register(r'animals', AnimalViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

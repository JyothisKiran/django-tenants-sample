from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserModelViewset

router = DefaultRouter()
router.register(r'auth', UserModelViewset)

urlpatterns = [
    path('domain/', include(router.urls))
]
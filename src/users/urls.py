from django.urls import path, include
from .views import UserModelViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', UserModelViewset)
urlpatterns = [
    path('u/', include(router.urls)),
    # path('login/', UserLoginView.as_view())
]
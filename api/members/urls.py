from django.urls.conf import include
from rest_framework import routers
from django.urls import path,include
from .views import  PrincipalViewSet, DependantsViewSet

router=routers.DefaultRouter()
router.register(r'',PrincipalViewSet)
router.register(r'',DependantsViewSet)

urlpatterns = [
    path(r'', include(router.urls))
]
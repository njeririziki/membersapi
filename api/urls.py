from django.urls.conf import include
from django.urls import path,include


urlpatterns = [
    path(r'members/', include(api.members.urls))
]
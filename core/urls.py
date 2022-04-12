from django.contrib import admin
from django.urls import path, include
import orcamentopessoal.urls
import dashboard.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(orcamentopessoal.urls)),
    path('', include(dashboard.urls)),
]

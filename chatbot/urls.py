from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('pizza.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^pizza/', include('pizza.urls')),
]

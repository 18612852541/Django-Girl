from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf import settings
from mysite.settings import MEDIA_ROOT



urlpatterns = [
    url(r'', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

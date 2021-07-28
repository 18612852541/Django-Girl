from django.conf.urls import url
from . import views
from rest_framework import routers

app_name = 'blog'

route = routers.DefaultRouter()

route.register(r'getarticleinfo' , views.GetArticleInfo)


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url('api/',include(route.urls))
]
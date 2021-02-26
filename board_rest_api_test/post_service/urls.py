from django.conf.urls import url

from post_service.views import post_list, post_detail

urlpatterns = [
    url(r'^$', post_list),
    url(r'^(?P<pk>[0-9]+)/$', post_detail),
]
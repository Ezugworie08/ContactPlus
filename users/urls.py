__author__ = 'Ikechukwu'
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

import users.views as views


urlpatterns = [
    url(r'^users/register/?$', views.RegisterContactOwner.as_view(), name='register'),
    url(r'^users/login/?$', views.LoginContactOwner.as_view(), name='login'),
    url(r'^users/update/?$', views.RegisterContactOwner.as_view(), name='register'),
    url(r'^users/logout/?$', views.LogoutContactOwner.as_view(), name='logout'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

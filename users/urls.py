__author__ = 'Ikechukwu'
from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

import users.views as views


urlpatterns = [
    url(r'^user/register/?$', views.RegisterContactOwner.as_view(), name='register'),
    url(r'^user/login/?$', views.LoginContactOwner.as_view(), name='login'),
    # url(r'^user/update/?$', views.UpdateContactOwner.as_view(), name='update'),
    url(r'^user/logout/?$', views.LogoutContactOwner.as_view(), name='logout'),
]
urlpatterns = format_suffix_patterns(urlpatterns)

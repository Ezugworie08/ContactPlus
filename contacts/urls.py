__author__ = 'Ikechukwu'
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import contacts.views as views


urlpatterns = [
    '',
    url(r'^contacts/?$', views.CreateListContact.as_view(), name='contact-create-list'),
    url(r'^contacts/(?P<pk>\d+)/?$', views.RetrieveUpdateDeleteContact.as_view(), name='single-contact'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
__author__ = 'Ikechukwu'
from django.conf.urls import patterns, url
import views
urlpatterns = patterns(
    '',
    url(r'^contacts/$', views.CreateListContact.as_view(), name='contact-create-list'),
    url(r'^contacts/(?P<pk>\d+)/$', views.RetrieveUpdateDeleteContact.as_view(), name='single-contact'),
)
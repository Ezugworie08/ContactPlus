from django.conf.urls import include, url
# from django.contrib import admin

urlpatterns = [
    url(r'^', include('contacts.urls', namespace='contacts')),
    url(r'^users/', include('users.urls', namespace='users')),
    # url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^web-api/', include('rest_framework.urls', namespace='rest_framework')),
]

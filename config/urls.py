from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^api/', include('articles.urls', namespace='articles')),
    url(r'^api/', include('authentication.urls', namespace='authentication')),
    url(r'^api/', include('profiles.urls', namespace='profiles')),
]
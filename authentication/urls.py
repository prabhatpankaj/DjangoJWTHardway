from django.conf.urls import url

from authentication.views import LoginAPIView, LogoutView, RegistrationAPIView, UserRetrieveUpdateAPIView

urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view(), name='profiles'),
    url(r'^users/register/?$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/?$', LoginAPIView.as_view(), name='login'),
    url(r'^users/logout/$', LogoutView.as_view(), name='logout'),
]
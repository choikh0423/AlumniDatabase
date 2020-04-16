from django.urls import path, re_path
from django.urls import include

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]

# re_path(r'^accounts/password_reset',
#         views.ResetPasswordRequestView.as_view(), name="password_reset"),


# re_path(r'^accounts/password_reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
#         views.ResetPasswordRequestView.as_view(), name="password_reset"),


# path('accounts/', include('django.contrib.auth.urls')),

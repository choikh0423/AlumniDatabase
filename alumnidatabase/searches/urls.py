from django.urls import path, re_path
from django.urls import include

from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('result/', views.alumnilist, name='search'),
    path('accounts/password_reset/',
         views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('directory/', views.directorylist, name='directory')
]

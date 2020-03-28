from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('signin/', views.signin),
    path('signout/', views.signout),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

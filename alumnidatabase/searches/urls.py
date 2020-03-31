from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]

# path('accounts/login/', views.CustomLoginView.as_view(), name='login'),

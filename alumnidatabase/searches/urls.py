from django.urls import path, re_path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('passwordresetfornm/', views.change_password1, name='passwordresetform'),
]

# path('accounts/login/', views.CustomLoginView.as_view(), name='login'),

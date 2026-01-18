
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(
    template_name='users/login.html'
       ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
>>>>>>> a3375b9dd01baa7fc5623089e58026df54af9896
]


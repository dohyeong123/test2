from django.contrib import admin
from django.urls import path,include
import testapp.views
from django.contrib.auth import views as auth_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',testapp.views.home, name='home'),
    path('login/',auth_view.LoginView.as_view(), name='login'),
    path('logout/',testapp.views.logout, name='logout'),
    path('signup/',testapp.views.signup, name='signup'),
    
]

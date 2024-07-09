from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.contrib.auth import views as auth_views
from myapp.views import loggedout
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp.views import loggedout
from django.contrib.auth.views import LogoutView  # Import LogoutView


class CustomLogoutView(LogoutView):
    next_page = '/loggedout/'  # Specify the URL where users should be redirected after logging out
    http_method_names = ['get', 'post']  # Allow both GET and POST requests

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.event_list, name='event_list'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name='profile'),
    path('rsvp/<int:event_id>/', views.rsvp, name='rsvp'),
    path('loggedout/', loggedout, name='loggedout'),
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

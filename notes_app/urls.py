from django.contrib import admin
from django.urls import path, include
from notes.views import RegisterAPIView, LoginAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('notes/', include('notes.urls')),
]
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', home, name='home'),  # Home page URL
    path('accounts/', include('django.contrib.auth.urls')),  # For built-in authentication URLs
]
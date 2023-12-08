from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_admin(request):
    return redirect('/admin/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('nonius_travel.urls')),
    path('', redirect_to_admin),  # Redirect root URL to admin
]


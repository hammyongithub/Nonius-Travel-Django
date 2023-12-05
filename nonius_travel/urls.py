from django.contrib import admin
from django.urls import path, include

from nonius_travel import views
from nonius_travel.views import UserSettingsAPIView

urlpatterns = [
    path('latestclients/', views.LatestClientsList.as_view()),
    path('hotelsearch/', views.hotel_search, name='hotelsearch'),
    path('offersearch/', views.offer_search, name='offersearch'),
    # Include Djoser auth paths
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # Add your custom user settings path
    path('auth/settings/', UserSettingsAPIView.as_view(), name='user-settings'),
]
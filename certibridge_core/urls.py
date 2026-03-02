from django.urls import path
from . import views

urlpatterns = [
    path('railway-embed/', views.embedded_railway_view, name='railway_embed'),
]
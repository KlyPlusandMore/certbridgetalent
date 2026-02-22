from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('trainings/', views.TrainingsView.as_view(), name='trainings'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/<int:course_id>/', views.RegisterView.as_view(), name='register_with_course'),
    path('register/success/', views.RegisterSuccessView.as_view(), name='register_success'),
]

from django.urls import path
from users.api import views

urlpatterns = [
    path('student-register/', views.StudentRegistrationView.as_view(), name='student-register'),
    path('student-login/', views.StudentLoginView.as_view(), name='student-login'),
    path('user-details/', views.UserDetailView.as_view(), name='user-details'),
    path('warden-register/', views.WardenRegistrationView.as_view(), name='warden-register'),
    path('warden-login/', views.WardenLoginView.as_view(), name='warden-login'),
]

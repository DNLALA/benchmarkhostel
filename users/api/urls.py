from django.urls import path
from users.api import views

urlpatterns = [
    path('student-register/', views.StudentRegistrationView.as_view(), name='student-register'),
    path('student-login/', views.StudentLoginView.as_view(), name='student-login'),
]

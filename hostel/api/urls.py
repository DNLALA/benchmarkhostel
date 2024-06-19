from django.urls import path
from hostel.api import views

urlpatterns = [
    path('hostel-create/', views.HostelCreateView.as_view(), name='hostel-create'),
]

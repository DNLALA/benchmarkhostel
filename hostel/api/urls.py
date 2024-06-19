from django.urls import path
from hostel.api import views

urlpatterns = [
    path('hostel-create/', views.HostelCreateUpdateView.as_view(), name='hostel-create'),
]

from django.urls import path
from hostel.api import views

urlpatterns = [
    path('change-hostel-user/<int:hostel_id>/', views.ChangeHostelUserView.as_view(), name='change-hostel-user'),
    path('hostel-detail-by-user/', views.HostelDetailByUserView.as_view(), name='hostel-detail-by-user'),
    path('hostel-create/', views.HostelCreateView.as_view(), name='hostel-create'),
    path('user-hostel-detail/', views.UserHostelDetailView.as_view(), name='user-hostel-detail'),
    path('hostel-list/', views.HostelListView.as_view(), name='hostel-list'),
]

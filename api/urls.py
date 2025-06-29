from django.urls import path
# Import the new DebugDBView
from .views import LoginView, DashboardSummaryView, DebugDBView 

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard-summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
    # Add this new path for our debug tool
    path('debug-db/', DebugDBView.as_view(), name='debug-db'),
]

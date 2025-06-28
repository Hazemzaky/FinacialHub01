from django.urls import path
from .views import LoginView, DashboardSummaryView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard-summary/', DashboardSummaryView.as_view(), name='dashboard-summary'),
]

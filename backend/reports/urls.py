from django.urls import path

from . import views

app_name = 'reports'

urlpatterns = [
    path('', views.ReportListView.as_view(), name='report_list'),
    path('<int:pk>/detail/', views.ReportDetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.ReportDeleteView.as_view(), name='delete'),
    path('<int:pk>/download/', views.download_report, name='download_report'),
    path('download/', views.download, name='download'),
    path('download/', views.download, name='download'),
]

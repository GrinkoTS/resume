from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='experience'),
    path('<int:pk>', views.FirmsDetailView.as_view(), name='job_description')
]
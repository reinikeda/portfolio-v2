from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('works/', views.WorksView.as_view(), name='works'),
]

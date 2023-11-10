from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('works/', views.WorksView.as_view(), name='works'),
    path('contacts/', views.ContactView.as_view(), name='contacts'),
]

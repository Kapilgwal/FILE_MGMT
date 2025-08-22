from django.urls import path 
from . import views
urlpatterns = [
    path('',views.UserView.as_view()),
    path('files/', views.FileView.as_view()),
]

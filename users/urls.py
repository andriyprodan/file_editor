from django.urls import path

from users import views

app_name = 'users'
urlpatterns = [
    path('activate/', views.Activate.as_view(), name='activate'),
]
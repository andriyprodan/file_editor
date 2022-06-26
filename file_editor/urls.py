from django.urls import path

from file_editor import views

app_name = 'files'
urlpatterns = [
    path('files/create/', views.FileCreate.as_view(), name='home'),
    path('files/<int:pk>/update/', views.FileUpdate.as_view(), name='update'),
    path('files/<int:pk>/', views.FileDetail.as_view(), name='detail'),
    path('files/', views.FileList.as_view(), name='list'),
]
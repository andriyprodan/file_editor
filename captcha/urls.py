from django.urls import path

from captcha import views

app_name = 'captcha'
urlpatterns = [
    path('check/', views.CaptchaCheck.as_view(), name='captcha_check'),
]
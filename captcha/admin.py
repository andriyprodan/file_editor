from django.contrib import admin

# Register your models here.
from captcha.models import Captcha, CaptchaImage

admin.site.register(Captcha)
admin.site.register(CaptchaImage)
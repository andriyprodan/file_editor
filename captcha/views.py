from django.shortcuts import render

# Create your views here.
from django.views import View

from captcha.forms import CaptchaForm
from captcha.models import Captcha


class CaptchaCheck(View):
    def get(self, request, *args, **kwargs):
        form = CaptchaForm(request.POST)
        # get random captcha
        captcha = Captcha.objects.order_by('?').first()
        form.instance = captcha
        images = captcha.images.order_by('?').all()
        return render(request, 'captcha/captcha_check.html', {'form': form, 'captcha': captcha, 'cap_images': images})

    def post(self, request, *args, **kwargs):
        form = CaptchaForm(request.POST)
        if form.is_valid():
            return render(request, 'captcha/captcha_success.html')
        return render(request, 'captcha/captcha_failed.html')

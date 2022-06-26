from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_migrate


def create_captcha_table(sender, **kwargs):
    from captcha.models import CaptchaImage
    from captcha.models import Captcha
    cap, _ = Captcha.objects.get_or_create(id=1, subject='Flower pot')
    correct_answers = [1, 2, 6, 9]
    for i in range(9):
        with open(settings.BASE_DIR / 'captcha/static/captcha_images/img{}.jpg'.format(i + 1), 'rb') as f:
            correct = True if i + 1 in correct_answers else False
            ci, _ = CaptchaImage.objects.get_or_create(id=i, cap=cap, correct_answer=correct)
            ci.image.save('img{}.jpg'.format(i + 1), f)


class CaptchaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'captcha'

    def ready(self):
        post_migrate.connect(create_captcha_table, sender=self)
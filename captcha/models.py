from django.db import models


# Create your models here.
class Captcha(models.Model):
    subject = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


class CaptchaImage(models.Model):
    cap = models.ForeignKey(Captcha, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()
    correct_answer = models.BooleanField(default=False)

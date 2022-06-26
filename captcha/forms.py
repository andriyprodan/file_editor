from django import forms

from captcha.models import Captcha, CaptchaImage


class CaptchaForm(forms.Form):
    def clean(self):
        cleaned_data = super().clean()
        images = cleaned_data['images']
        captcha = cleaned_data['captcha']

        correct_images = captcha.images.filter(correct_answer=True)
        if list(images.all()) != list(correct_images.all()):
            raise forms.ValidationError('Incorrect answer')
        return cleaned_data

    images = forms.ModelMultipleChoiceField(queryset=CaptchaImage.objects.all())
    captcha = forms.ModelChoiceField(queryset=Captcha.objects.all())


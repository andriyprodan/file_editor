from django.shortcuts import render

# Create your views here.
from django.views import View

from users.forms import ActivateForm
from users.models import IsActivated

ALPHABET = ' abcdefghijklmnopqrstuvwxyz'


def vigenere_cipher(text, key):
    # vigenere cipher with whitespace
    cipher = ''
    for i, c in enumerate(text):
        if c.isalpha() or c.isspace():
            idx = ALPHABET.index(c.lower())
            letter = ALPHABET[(idx + ALPHABET.index(key[i % len(key)])) % len(ALPHABET)]
            cipher += letter.upper() if c.isupper() else letter
        else:
            cipher += c
    return cipher


KEYWORD = 'iron'
ACTIVATION_CODE = 'Iron is a vital trace element for humans'
ENCRYPTED_CODE = vigenere_cipher(ACTIVATION_CODE, KEYWORD)


class Activate(View):
    def get(self, request, *args, **kwargs):
        form = ActivateForm()
        return render(request, 'users/activate.html', {'form': form})

    def post(self, request, *args, **kwargs):
        f = ActivateForm(request.POST)
        if f.is_valid():
            code = f.cleaned_data['code']
            if vigenere_cipher(code, KEYWORD) == ENCRYPTED_CODE:
                IsActivated.objects.update_or_create(is_activated=True)
                return render(request, 'users/activate_success.html')
            f.add_error('code', 'Invalid activation code')

        return render(request, 'users/activate.html', {'form': f})
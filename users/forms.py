from django import forms


class ActivateForm(forms.Form):
    code = forms.CharField(max_length=255, help_text='Enter activation code')

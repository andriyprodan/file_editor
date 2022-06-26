from ckeditor.widgets import CKEditorWidget
from django import forms
from django.core.files.base import ContentFile

from file_editor.models import HtmlFile


class EditorForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.id:
            self.fields['content'].initial = self.instance.content

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.file:
            with open(instance.file.path, 'w') as f:
                f.write(self.cleaned_data['content'])
        else:
            instance.file.save('filename.html', ContentFile(self.cleaned_data['content']))
        if commit:
            instance.save()
        return instance

    class Meta:
        model = HtmlFile
        fields = ('content',)



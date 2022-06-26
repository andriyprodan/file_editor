import os
from datetime import datetime

from django.db import models


# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe


class HtmlFile(models.Model):
    file = models.FileField(upload_to='files/')

    @property
    def content(self):
        with open(self.file.path, 'r') as f:
            return mark_safe(f.read())

    @property
    def info(self):
        foo = os.path.getmtime(self.file.path)
        def convert_date(date):
            return datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
        return mark_safe(f"""
            <b>Size:</b> {os.path.getsize(self.file.path)}<br/>
            <b>Last Modified:</b> {convert_date(os.path.getmtime(self.file.path))}<br/>
            <b>Created:</b> {convert_date(os.path.getctime(self.file.path))}<br/>
        """)

    def get_absolute_url(self):
        return reverse('files:update', args=(self.pk,))
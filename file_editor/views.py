# Create your views here.
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from file_editor.forms import EditorForm
from file_editor.models import HtmlFile


class FileCreate(CreateView):
    form_class = EditorForm
    template_name = 'file_editor/home.html'


class FileDetail(DetailView):
    queryset = HtmlFile.objects.all()
    template_name = 'file_editor/file_detail.html'


class FileUpdate(UpdateView):
    form_class = EditorForm
    queryset = HtmlFile.objects.all()
    template_name = 'file_editor/file_edit.html'


class FileList(ListView):
    queryset = HtmlFile.objects.all()
    template_name = 'file_editor/html_file_list.html'

    def get_queryset(self):
        query = self.request.GET.get('filename', '')
        return HtmlFile.objects.filter(file__icontains=query)

import json
from io import BytesIO

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import FileResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, ListView
from docx import Document

from .examination import exam
from .forms import ReportForm
from .models import Report


@login_required
def download(request):
    if request.method == 'POST':
        form = ReportForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            doc = Document(form.cleaned_data['file'])
            info = exam(doc)
            obj = Report.objects.create(
                author=request.user,
                title=''.join(str(form.cleaned_data['file']).split('.')[:-1]),
                text=json.dumps(info, ensure_ascii=False),
            )
            return redirect('reports:detail', obj.id)
    else:
        form = ReportForm()

    return render(
        request,
        'reports/download.html',
        {'form': form}
    )


@login_required
def download_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if report.author != request.user and not request.user.is_superuser:
        raise PermissionDenied

    report.text = json.loads(report.text)
    response = BytesIO()
    response.write('Основной текст:\n\n'.encode())
    if report.text['par_info']:
        for info in report.text['par_info']:
            if 'warning' in info:
                response.write('Предупреждение: '
                               f'{info["warning"]}\n'.encode())
                text = info["text"] if info["text"] else "Пустая строка."
                response.write(f'Текст: {text}\n'.encode())
                next_text = (info["next_text"]
                             if "next_text" in info and info["next_text"]
                             else "Пустая строка.")
                response.write(f'Следующий текст: {next_text}'
                               '\n\n'.encode())
            else:
                response.write(f'Стиль: {info["style"]}\n'.encode())
                response.write('Ошибки:\n'.encode())
                for _, error in info['errors'].items():
                    response.write(f'{error["name"]}: '
                                   f'{error["error_text"]}\n'.encode())
                response.write(f'Текст: {info["text"]}\n\n'.encode())
    else:
        response.write('Текст оформлен по требованиям.\n'.encode())
    if report.text['tab_info']:
        response.write('\n\n\nТаблицы:\n\n'.encode())
        for table in report.text['tab_info']:
            if ('rows' in table[1] and table[1]['rows']
                    or 'table_alignment' in table[1]):
                response.write(f'Таблица {int(table[0].split("_")[-1])+1}'
                               ':\n'.encode())
                if 'table_alignment' in table[1]:
                    response.write('Выравнивание: '
                                   f'{table[1]["table_alignment"]}'
                                   '\n'.encode())
                for i, row in table[1]['rows'].items():
                    response.write(f'Строка {int(i.split("_")[-1])+1}:'
                                   '\n'.encode())
                    for j, cell in row.items():
                        response.write(f'Колонка {int(j.split("_")[-1])+1}:'
                                       '\n'.encode())
                        for info in cell:
                            response.write('Ошибки:\n'.encode())
                            for _, error in info['errors'].items():
                                response.write(f'{error["name"]}: '
                                               f'{error["error_text"]}'
                                               '\n'.encode())
                            response.write(f'Текст: {info["text"]}'
                                           '\n\n'.encode())
            else:
                response.write(f'Таблица {int(table[0].split("_")[-1])+1} '
                               'оформлена по требованиям.\n'.encode())
    response.seek(0)

    return FileResponse(
        response,
        as_attachment=True,
        filename=f'{report.title}.txt'
    )


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    paginate_by = 5

    def get_queryset(self):
        return self.request.user.reports.all()


class ReportDeleteView(LoginRequiredMixin, DeleteView):
    model = Report
    success_url = reverse_lazy('reports:report_list')

    def dispatch(self, request, *args, **kwargs):
        instance = get_object_or_404(Report, pk=kwargs['pk'])
        if instance.author != request.user and not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ReportDetailView(DetailView):
    model = Report

    def dispatch(self, request, *args, **kwargs):
        instance = get_object_or_404(Report, pk=kwargs['pk'])
        if instance.author != request.user and not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        report = context['report']
        report.text = json.loads(report.text)
        context['report'] = report
        return context

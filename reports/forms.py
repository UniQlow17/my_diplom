from django import forms
from django.core.validators import FileExtensionValidator


class ReportForm(forms.Form):
    file = forms.FileField(
        label='Файл',
        validators=[FileExtensionValidator(['docx'])],
        help_text="Поддерживаемый формат файлов: docx"
    )

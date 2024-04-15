from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import FeedbackForm


class RulesPage(TemplateView):
    template_name = 'core/rules.html'


def get_feedback(request):
    flag = False
    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            flag = True
    else:
        form = FeedbackForm()

    return render(
        request,
        'core/feedback.html',
        {'form': form, 'flag': flag}
    )


def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=403)


def server_error(request):
    return render(request, 'core/500.html', status=500)

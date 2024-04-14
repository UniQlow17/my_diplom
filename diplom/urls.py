from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import include, path, reverse_lazy
from django.views.generic.edit import CreateView

from core.views import RulesPage, get_feedback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rules/', RulesPage.as_view(), name='rules'),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration/',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('rules'),
        ),
        name='registration',
    ),
    path('reports/', include('reports.urls')),
    path('me/', include('users.urls')),
    path('feedback/', get_feedback, name='feedback'),
]

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT)

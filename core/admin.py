from django.contrib import admin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Регистрация модели отзывов на панеле администратора.
    """

    list_display_links = ('username',)
    list_display = (
        'id',
        'username',
        'text',
    )
    search_fields = ('username',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Регистрация модели подписок на панеле администратора.
    """

    list_display_links = ('username',)
    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'last_login',
        'date_joined',
        'is_staff',
    )
    exclude = ('groups', 'user_permissions', 'password',)
    search_fields = ('username',)
    list_filter = ('email', 'username',)
    empty_value_display = '-пусто-'

from django.contrib import admin

from .models import Param, Report, Rule, Style


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    """
    Регистрация модели отчетов на панеле администратора.
    """

    list_display_links = ('title',)
    list_display = (
        'id',
        'title',
        'author',
        'pub_date',
    )
    search_fields = ('author',)
    list_filter = ('author',)
    empty_value_display = '-пусто-'


@admin.register(Param)
class ParamAdmin(admin.ModelAdmin):
    """
    Регистрация модели параметров на панеле администратора.
    """

    list_display_links = ('name',)
    list_display = (
        'id',
        'name',
        'slug'
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    """
    Регистрация модели стилей на панеле администратора.
    """

    list_display_links = ('name',)
    list_display = (
        'id',
        'name',
        'slug'
    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    """
    Регистрация модели правил на панеле администратора.
    """

    list_display_links = ('style',)
    list_display = (
        'id',
        'style',
        'param',
        'value',
    )
    search_fields = ('style',)
    list_filter = ('style', 'param',)
    empty_value_display = '-пусто-'

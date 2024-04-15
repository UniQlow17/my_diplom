from django import template

register = template.Library()


@register.filter()
def get_last_obj(value, param):
    return value.split(param)[-1]

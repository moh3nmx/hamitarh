from django import template
from django.db.models import Q

register = template.Library()


@register.filter
def to_slash(value):
    return str(value).replace('-', '/')


@register.filter
def verbose_name(value, x):
    return value._meta.get_field(x).verbose_name

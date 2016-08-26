from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='cut')
@stringfilter
def cut(value):
    return '{:.200}'.format(value)

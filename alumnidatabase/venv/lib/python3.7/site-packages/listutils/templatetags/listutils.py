from django import template
from django.core.paginator import Paginator

register = template.Library()

@register.filter
def partition(objects, n):
    paginator = Paginator(objects, n)
    for indi in paginator.page_range:
        yield paginator.page(indi)
    






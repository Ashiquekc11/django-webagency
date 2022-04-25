from django import template

register = template.Library()

@register.filter
def process(value):
    value = ''.join([i for i in value if not i.isdigit()])
    return value.upper()

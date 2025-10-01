from django import template

register=template.Library()

@register.filter()
def multiply(v1,v2):
    return v1*v2
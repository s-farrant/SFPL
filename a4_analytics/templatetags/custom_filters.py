from django import template

register = template.Library()

@register.filter
def get_item(obj, attr_name):
    attrs = attr_name.split('.')
    for attr in attrs:
        if isinstance(obj, dict):
            obj = obj.get(attr)
        else:
            return None
    return obj
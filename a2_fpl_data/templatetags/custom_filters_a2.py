from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter
def suffix(value):
    try:
        value = int(value)
        if 10 <= value % 100 <= 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(value % 10, "th")
        return mark_safe(f"{value}<sup>{suffix}</sup>")
    except (ValueError, TypeError):
        return value
    

@register.filter
def lookup(obj, key):
    try:
        if isinstance(obj, dict):
            return obj.get(key, "")
        return getattr(obj, key, "")
    except Exception:
        return ""
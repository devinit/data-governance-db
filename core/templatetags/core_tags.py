from django import template
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


register = template.Library()


@register.filter
def is_valid_url(value):
    validator = URLValidator()
    try:
        validator(value)
        return True
    except ValidationError:
        return False

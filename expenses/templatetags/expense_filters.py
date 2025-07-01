from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    """
    Multiplies the value by the argument
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''

@register.filter(name='add_class')
def add_class(field, css_class):
    """
    Adds a CSS class to a Django form field
    """
    return field.as_widget(attrs={"class": css_class})
from django import template

register = template.Library()

@register.filter
def modulo(num, val):
    return num % val

#Need to add app1 in installed_apps and {% load mytags%} in template
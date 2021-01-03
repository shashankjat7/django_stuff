from django import template

register = template.Library()

@register.filter(name='cut_it')
def cut_it(value,arg):
    """
    this cuts our all values of args from the string
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg,'')


# register.filter('cut_it',cut_it)
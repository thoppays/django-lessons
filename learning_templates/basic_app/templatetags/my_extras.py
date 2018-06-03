from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value, arg):
    """This function cuts the arg from the value"""
    return value.replace(arg, "")

# The following is the alternate way instead of using decorator above
# register.filter("cut", cut)

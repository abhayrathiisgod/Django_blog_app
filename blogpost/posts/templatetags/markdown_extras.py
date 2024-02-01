from django import template
from django.template.defaultfilters import stringfilter
import markdown as md
from posts.models import Category

register = template.Library()
 
@register.simple_tag
def get_categories():
    return Category.objects.all()[0:3]
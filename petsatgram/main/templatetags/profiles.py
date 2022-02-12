from django import template

from petsatgram.main.models import Profile

register = template.Library()

# reusable code , can include a template inside
@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0

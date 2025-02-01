# nss/templatetags/custom_tags.py
from django import template
from nss.models import volunteer  # Adjust this to match your app structure

register = template.Library()

@register.simple_tag
def volunteers_for_year_and_unit(program_name, year, unit):
    return volunteer.objects.filter(program__program_name=program_name, year=year, unit=unit)

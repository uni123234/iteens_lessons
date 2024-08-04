from django import template
from django.core.paginator import Paginator
from ..models import Student, Teacher

register = template.Library()


@register.simple_tag
def total_students():
    return Student.objects.count()


@register.simple_tag
def total_teachers():
    return Teacher.objects.count()


@register.inclusion_tag('students_pagination.html', takes_context=True)
def students_pagination(context, students, page_num):
    paginator = Paginator(students, 10)
    page_obj = paginator.get_page(page_num)
    return {'page_obj': page_obj, 'request': context['request']}

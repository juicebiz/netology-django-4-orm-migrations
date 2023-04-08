from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    context = {
        #'object_list': Student.objects.order_by(ordering).all()
        'object_list': Student.objects.order_by(ordering).all().prefetch_related('teachers')
    }

    return render(request, template, context)

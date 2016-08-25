from django.shortcuts import render,get_object_or_404
from .models import Course

def index(request):
    courses = Course.objects.all()
    template_name = 'index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

# def details(request, pk):
#     #course = Course.objects.get(pk=pk)
#     course = get_object_or_404(Course, pk=pk)
#     template_name = 'details.html'
#     context = {
#         'course': course
#     }
#     return render(request,template_name,context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    template_name = 'details.html'
    context = {
        'course': course
    }
    return render(request,template_name,context)

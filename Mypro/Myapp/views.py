from django.shortcuts import render
from django.views.generic import DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.
def courselist(request):
    courses = course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

class CourseDeleteView(DeleteView):
    model = course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course-list')
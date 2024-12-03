from django.urls import path
from .views import *
urlpatterns = [
    path('course/', courselist, name='course-list'),
    path('coursedelete/<str:pk>', CourseDeleteView.as_view(), name='course-delete')
]
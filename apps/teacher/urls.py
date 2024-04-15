from django.urls import path
from . views import TeacherView


urlpatterns = [
    path("teacher/list/", TeacherView.as_view(template_name="teacher-list.html"), name="app-teacher-list"),
]

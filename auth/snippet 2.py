from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class DashboardsView(TemplateView):
    template_name = "dashboard_analytics.html"  # Default template name

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Your additional context data if needed
        return context

    def get(self, request, *args, **kwargs):
        # Handle GET request
        context = self.get_context_data(**kwargs)
        # Your logic for handling GET request
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Handle POST request
        context = self.get_context_data(**kwargs)
        # Your logic for handling POST request
        return render(request, self.template_name, context)

    # Implement other HTTP methods (PUT, DELETE, etc.) as needed


from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

class AcademyView(TemplateView):
    template_name = "app_academy_dashboard.html"  # Default template name

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Your additional context data if needed
        return context


from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

class AcademyView(TemplateView):
    template_name = "app_academy_dashboard.html"  # Default template name

    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return login_required(view)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Your additional context data if needed
        return context

class CourseView(AcademyView):
    template_name = "app_academy_course.html"

class CourseDetailsView(AcademyView):
    template_name = "app_academy_course_details.html"

from django.urls import path
from .views import AcademyView, CourseView, CourseDetailsView

urlpatterns = [
    path("app/academy/dashboard/", AcademyView.as_view(), name="app-academy-dashboard"),
    path("app/academy/course/", CourseView.as_view(), name="app-academy-course"),
    path("app/academy/course_details/", CourseDetailsView.as_view(), name="app-academy-course-details"),
    # Other URL patterns
]

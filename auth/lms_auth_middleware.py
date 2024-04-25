from django.http import HttpResponseRedirect
from django.urls import reverse

class StudentRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is authenticated and in the "student" group
        if request.user.is_authenticated and request.user.groups.filter(name='Student').exists():
            # Redirect to the student dashboard
            if not request.path.startswith(reverse('app-academy-dashboard')):
                return HttpResponseRedirect(reverse('app-academy-dashboard'))

        return response


class RoleRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check for additional roles/groups
            if request.user.groups.filter(name='Student').exists():
                # Redirect to the student dashboard
                if not request.path.startswith(reverse('app-academy-dashboard')):
                    return HttpResponseRedirect(reverse('app-academy-dashboard'))
            elif request.user.groups.filter(name='Instructor').exists():
                # Redirect to the instructor dashboard
                if not request.path.startswith(reverse('dashboard-instructor')):
                    return HttpResponseRedirect(reverse('dashboard-instructor'))
            elif request.user.groups.filter(name='new_role'):
                if not request.path.startswith(reverse("new_role_dashboard")):
                    return HttpResponseRedirect(reverse("new_role_dashboard"))
                

        return response

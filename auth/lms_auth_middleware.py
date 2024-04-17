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
            if not request.path.startswith(reverse('dashboard-student')):
                return HttpResponseRedirect(reverse('dashboard-student'))

        return response

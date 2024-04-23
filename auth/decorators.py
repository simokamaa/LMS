# decorators.py
from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.models import Group

def group_required(group_names):
    """
    Decorator for views that checks if the user is in the required group.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                # Redirect to login page if user is not authenticated
                return redirect('login')

            user_groups = request.user.groups.values_list('name', flat=True)
            # Check if user is in any of the required groups
            if not any(group in user_groups for group in group_names):
                # Redirect to unauthorized page or raise PermissionDenied exception
                return redirect('unauthorized')  # You can replace 'unauthorized' with your own URL name or raise PermissionDenied

            return view_func(request, *args, **kwargs)
        return wrapped_view
    return decorator

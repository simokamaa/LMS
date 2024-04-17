from django.shortcuts import redirect

class StudentMiddleware:
    def __process_view(self, request, view_func, view_args, view_kwargs):
        # Check if user is logged in and is a student
        if request.user.is_authenticated and request.user.is_staff:  # Replace 'is_staff' with your student check logic
            return redirect('index')  # Replace 'index' with your desired redirect URL
        return None

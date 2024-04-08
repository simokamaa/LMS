from django.conf import settings

class LmsAuthenticationMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            response.set_cookie(settings.SESSION_COOKIE_NAME, request.user.session_key, max_age=settings.SESSION_COOKIE_AGE)
        else:
            response.delete_cookie(settings.SESSION_COOKIE_NAME)
        return response
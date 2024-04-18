from django.urls import path
from . views import LmsAppView


urlpatterns = [
    path("", LmsAppView.as_view(template_name=""), name="lms_app_index"),
]

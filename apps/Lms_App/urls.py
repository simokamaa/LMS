from django.urls import path
from . views import LmsAppView


urlpatterns = [
    path("", LmsAppView.as_view(template_name="lms_modules_management.html"), name="lms_module"),
    path("app/new/", LmsAppView.as_view(template_name="modal_create_app.html"), name="lms_app_index"),
]

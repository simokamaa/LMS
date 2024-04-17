from django.urls import path
from .views import DashboardsView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path(
        "",
        login_required(DashboardsView.as_view(template_name="dashboard_analytics.html")),
        name="index",
    ),

    path(
        "dashboard/crm/",
        login_required(DashboardsView.as_view(template_name="dashboard_crm.html")),
        name="dashboard-crm",
    ),
    
    path(
        "dashboard/student",
        login_required(DashboardsView.as_view(template_name="dashboard_analytics.html")),
        name="dashboard-student",
    ),

    path( 
        "dashboard/instructor/",
        login_required(DashboardsView.as_view(template_name="dashboard_crm.html")),
        name="dashboard-instructor",
    ),
    
        path( 
        "dashboard/general/",
        login_required(DashboardsView.as_view(template_name="dashboard_general.html")),
        name="dashboard-general",
    ),
    path( 
        "dashboard/role/",
        login_required(DashboardsView.as_view(template_name="new_role_dashboard.html")),
        name="new_role_dashboard",
    ),
]

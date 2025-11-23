from django.urls import path
from .views import (
    dashboard_view,
    register_view,
    login_view,
    profile_view,
    calorie_entry_view,
    logout_view,
)

urlpatterns = [
    # Authentication ============
    path("auth/login/", login_view, name="login"),
    path("auth/register/", register_view, name="register"),
    path("auth/logout/", logout_view, name="logout"),
    
    # Main Method ===============
    path("profile/", profile_view, name="profile"),
    path("", dashboard_view, name="dashboard"),
    path("calorie/entry", calorie_entry_view, name="calorie_entry"),
]

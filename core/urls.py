from django.urls import path
from . import views
from prototype.views import filter_view
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('login_user', views.LoginUser.as_view(), name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register_user', staff_member_required(views.RegisterUser.as_view()), name="register_user"),
    path('home', views.home, name='home'),
    path('projects/<int:project_id>/prototypes', filter_view, name="filter"  )
]
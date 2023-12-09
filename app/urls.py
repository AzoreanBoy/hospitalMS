from django.urls import include, path

from . import views

urlpatterns = [
    # HOME PAGE for unauthenticated users
    path("hms", views.landing, name="landing"),
    # HOME PAGE for authenticated users
    path("", views.index, name="index"),
    
    #login/Logout
    path("login/",views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    
]
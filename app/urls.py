from django.urls import include, path

from . import views

urlpatterns = [
    # HOME PAGE for unauthenticated users
    path("HMS", views.landing, name="landing"),
    # HOME PAGE for authenticated users
    path("", views.index, name="index"),
    
    #login/Logout
    path("login/",views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    
    path('patients/', views.patients, name ='patients'),
    path('admissions/',views.admissions, name = 'admissions'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('physicians/', views.physicians, name='physicians'),
    path('exams/', views.exams, name = 'exams'),
    path('diagnosis/', views.diagnosis, name="diagnosis"),
    
]
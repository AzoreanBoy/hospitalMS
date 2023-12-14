from django.urls import include, path

from . import views

urlpatterns = [
    path("example", views.example, name="example"),
    # HOME PAGE for unauthenticated users
    path("HMS", views.landing, name="landing"),
    # HOME PAGE for authenticated users
    path("", views.index, name="index"),
    
    #login/Logout
    path("login/",views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    
    #Lists of the Entities in the DB
    path('patients/', views.patients, name ='patients'),
    path('admissions/',views.admissions, name = 'admissions'),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    path('physicians/', views.physicians, name='physicians'),
    path('exams/', views.exams, name = 'exams'),
    path('diagnosis/', views.diagnosis, name="diagnosis"),
    
    # PACIENTES
    path('patientdetails/<str:pk>', views.patientdetails, name = 'patientdetails'),
    path('addpatient/', views.addPatient, name="addPatient"),
    
    # MÉDICOS
    path("physiciandetails/<str:pk>", views.physiciandetails, name="physiciandetails"),
]
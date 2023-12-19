from django.urls import include, path

from . import views

urlpatterns = [
    # HOME PAGE for unauthenticated users
    #path("HMS", views.landing, name="landing"),

    # HOME PAGE for authenticated users
    path("", views.index, name="index"),
    
    #login/Logout
    path("login/",views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    
    #Lists of the Entities in the DB
    path('admissions/',views.admissions, name = 'admissions'),
    path('physicians/', views.physicians, name='physicians'),
    path('patients/', views.patients, name ='patients'),
    path('exams/', views.exams, name = 'exams'),
    path('diagnosis/', views.diagnosis, name="diagnosis"),
    path('prescriptions/', views.prescriptions, name='prescriptions'),
    
    # ADMISSIÕES
    path("newadmission/", views.newAdmission, name="newAdmission"),
    
    # PACIENTES
    path('patientdetails/<str:pk>', views.patientdetails, name = 'patientdetails'),
    path('addpatient/', views.addPatient, name="addPatient"),
    
    # MÉDICOS
    path("physiciandetails/<str:pk>", views.physiciandetails, name="physiciandetails"),
]
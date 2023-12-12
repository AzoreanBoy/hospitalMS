from django.http import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *

from .decorators import *

from .forms import NewPatientForm

# Create your views here.


def landing(request):
    return render(request, "app/landing.html")


@login_required(login_url="landing")
def index(request):
    return render(request, "app/index.html")


@unauthenticatedUser
def loginUser(request):
    if request.method == "POST":
        us = request.POST["usernamelogin"]
        pa = request.POST["password"]

        user = authenticate(request, username=us, password=pa)

        if user is not None:
            print("User is not none")
            login(request, user)
            return redirect("index")
        else:
            messages.warning(request, "Username or password are incorrect.")
    return render(request, "app/login.html")


def logoutUser(request):
    logout(request)
    return redirect("landing")


# Lists
def admissions(request):
    admissions = Admission.objects.all()
    return HttpResponse("Admissões")


def patients(request):
    patients = Patient.objects.all()
    return render(request, "app/patients.html", {"patients": patients})


def physicians(request):
    physicians = Physician.objects.all()
    return HttpResponse("Physicians")


def prescriptions(request):
    prescriptions = Prescription.objects.all()
    pm = PrescriptionMedication.objects.all()
    medicaments = Medication.objects.all()
    return HttpResponse("Prescriptions")


def exams(request):
    return HttpResponse("Exams")


def diagnosis(request):
    return HttpResponse("Diagnosis")


def addPatient(request):
    form = NewPatientForm
    if request.method == "POST":
        form = NewPatientForm(request.POST)
        
        print(request.POST['person_adress'])
        
        
        if form.is_valid():
            print("Formulário Válido")
            patient = Patient(person_id_card_number=request.POST['person_id_card_number'],
                              person_healthcare_number = request.POST['person_healthcare_number'],
                              person_adress = request.POST['person_adress'],
                              person_phone_number = request.POST['person_phone_number'],
                              person_name = request.POST['person_name'],
                              person_birth_date = request.POST['birthdate'],
                              person_sex = request.POST['sex'])
            
            patient.save()
            print(patient)
            
            return redirect('patients')
            
                    
        else:
            print(form.errors)
            messages.error(request,form.errors)
        
    return render(request, "app/addpatient.html",{
        "form":NewPatientForm
    })

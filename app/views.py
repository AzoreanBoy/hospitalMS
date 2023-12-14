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


def patientdetails(request, pk):
    patient = Patient.objects.get(id_card_number=pk)
    print(patient.sex)
    return render(
        request,
        "app/patientdetails.html",
        {
            "patient": patient,
        },
    )


def addPatient(request):
    form = NewPatientForm
    if request.method == "POST":
        form = NewPatientForm(request.POST)

        print(request.POST["adress"])

        if form.is_valid():
            print("Formulário Válido")
            patient = Patient(
                id_card_number=request.POST["id_card_number"],
                healthcare_number=request.POST["healthcare_number"],
                adress=request.POST["adress"],
                phone_number=request.POST["phone_number"],
                name=request.POST["name"],
                birth_date=request.POST["birthdate"],
                sex=request.POST["sex"],
                nationality=request.POST["nationality"],
            )

            patient.save()
            print(patient)

            return redirect("patients")

        else:
            print(form.errors)
            messages.error(request, form.errors)

    return render(request, "app/addpatient.html", {"form": NewPatientForm})


def physicians(request):
    physicians = Physician.objects.all()
    return render(
        request,
        "app/physicians.html",
        {
            "physicians": physicians,
        },
    )


def physiciandetails(request, pk):
    physician = Physician.objects.get(id_card_number=pk)
    return render(
        request,
        "app/physiciandetails.html",
        {
            "doctor": physician,
        },
    )


def prescriptions(request):
    prescriptions = Prescription.objects.all()
    pm = PrescriptionMedication.objects.all()
    medicaments = Medication.objects.all()
    return HttpResponse("Prescriptions")


def exams(request):
    return HttpResponse("Exams")


def diagnosis(request):
    return HttpResponse("Diagnosis")

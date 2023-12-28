from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .decorators import *
from .forms import NewPatientForm, NewAdmissionForm
from .models import *


# Create your views here.

# def landing(request):
#     return render(request, "app/landing.html")


# @login_required(login_url="landing")
def index(request):
    return render(request, "app/index.html")


# @unauthenticatedUser
# def loginUser(request):
#     if request.method == "POST":
#         us = request.POST["usernamelogin"]
#         pa = request.POST["password"]
#
#         user = authenticate(request, username=us, password=pa)
#
#         if user is not None:
#             print("User is not none")
#             login(request, user)
#             return redirect("index")
#         else:
#             messages.warning(request, "Username or password are incorrect.")
#     return render(request, "app/login.html")


# def logoutUser(request):
#     logout(request)
#     return redirect("landing")


# ADMISSIONS -----------------------------------------------------------------------------------------------------------
def admissions(request):
    admissions = Admission.objects.all().order_by("-adm_date", "patient")
    return render(request, "app/admissions.html", {"admissions": admissions, }, )


def admisisonDetails(request, id):
    admission = Admission.objects.get(id=id)
    exams = Exam.objects.filter(admission=admission).order_by("-exam_date")
    diagnosis = Diagnosis.objects.filter(admission=admission).order_by("-date")
    prescriptions = Prescription.objects.filter(admission=admission).order_by("-id")
    return render(request, "app/admissiondetails.html",
                  {"admission": admission, "exams": exams, "diagnosis": diagnosis, "prescriptions": prescriptions})


def newAdmission(request):
    form = NewAdmissionForm()
    if request.method == "POST":
        print(request.POST)
        form = NewAdmissionForm(request.POST)
        if form.is_valid():
            adm = form.save(commit=False)
            adm.save()
            return redirect("admissions")
    return render(request, "app/newadmission.html", {'form': form, })


# PACIENTES ------------------------------------------------------------------------------------------------------------
def patients(request):
    patients = Patient.objects.all()
    return render(request, "app/patients.html", {"patients": patients})


def patientdetails(request, pk):
    patient = Patient.objects.get(id_card_number=pk)
    admissions = Admission.objects.filter(patient=patient).order_by('-adm_date')
    return render(request, "app/patientdetails.html", {"patient": patient, "admissions": admissions}, )


def addPatient(request):
    form = NewPatientForm
    if request.method == "POST":
        form = NewPatientForm(request.POST)

        print(request.POST["adress"])

        if form.is_valid():
            print("Formulário Válido")
            patient = Patient(id_card_number=request.POST["id_card_number"],
                              healthcare_number=request.POST["healthcare_number"], adress=request.POST["adress"],
                              phone_number=request.POST["phone_number"], name=request.POST["name"],
                              birth_date=request.POST["birthdate"], sex=request.POST["sex"],
                              nationality=request.POST["nationality"], )

            patient.save()
            print(patient)

            return redirect("patients")

        else:
            print(form.errors)
            messages.error(request, form.errors)

    return render(request, "app/addpatient.html", {"form": NewPatientForm})


# MÉDICOS --------------------------------------------------------------------------------------------------------------
def physicians(request):
    physicians = Physician.objects.all()
    return render(request, "app/physicians.html", {"physicians": physicians, }, )


def physiciandetails(request, pk):
    physician = Physician.objects.get(id_card_number=pk)

    return render(request, "app/physiciandetails.html", {"doctor": physician, }, )


# PRESCRIÇÕES ----------------------------------------------------------------------------------------------------------
def prescriptions(request):
    prescriptions = Prescription.objects.all().order_by('-prescription_date')
    return render(request, "app/prescriptions.html", {"prescriptions": prescriptions, })


def prescriptiondetails(request, pk):
    prescription = Prescription.objects.get(pk=pk)
    medications = PrescriptionMedication.objects.filter(prescription=prescription)
    return render(request, "app/prescriptiondetails.html", {"prescription": prescription, "medications": medications, })


# EXAMES ---------------------------------------------------------------------------------------------------------------
def exams(request):
    exams = Exam.objects.all().order_by('-exam_date')
    return render(request, "app/exams.html", {"exams": exams, }, )


def examdetails(request, pk):
    exam = Exam.objects.get(pk=pk)
    return render(request, "app/examdetails.html", {"exam": exam})


# DIAGNÓSTICOS ---------------------------------------------------------------------------------------------------------
def diagnosis(request):
    diagnosis = Diagnosis.objects.all().order_by('-date')
    return render(request, "app/diagnosis.html", {"diagnosis": diagnosis, })


def diagnosisdetails(request, pk):
    diagnosis = Diagnosis.objects.get(pk=pk)
    exams = Exam.objects.filter(admission=diagnosis.admission)
    return render(request, "app/diagnosisdetails.html", {"diagnosis": diagnosis, "exams": exams})

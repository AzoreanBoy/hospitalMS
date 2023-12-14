from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Domains
class Speciality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        # managed = False
        db_table = "speciality"

    def __str__(self):
        return self.name


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    class Meta:
        # managed = False
        db_table = "department"

    def __str__(self):
        return self.name


class Medication(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)

    class Meta:
        # managed = False
        db_table = "medication"

    def __str__(self):
        return self.name


class ExamsCode(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=512)

    class Meta:
        # managed = False
        db_table = "exams_code"

    def __str__(self):
        return self.description


class DiagnosisCode(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        # managed = False
        db_table = "diagnosis_code"

    def __str__(self):
        return self.description


# Relational Models


class Patient(models.Model):
    class SEX(models.TextChoices):
        FEMALE = "f", _("Female")
        MALE = "m", _("Male")

    id_card_number = models.CharField(
        primary_key=True,
        max_length=8,
        validators=[MinLengthValidator(8), MaxLengthValidator(8)],
    )
    healthcare_number = models.CharField(
        max_length=9,
        validators=[MinLengthValidator(9), MaxLengthValidator(9)],
        null=False,
        blank=False,
    )
    name = models.CharField(max_length=512, null=False)
    adress = models.CharField(max_length=512, blank=True, null=True)
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    birth_date = models.DateField(null=False, blank=False)
    nationality = models.CharField(max_length=256, blank=True, null=True)
    sex = models.CharField(max_length=1, null=False, choices=SEX.choices, default="-")

    class Meta:
        db_table = "patient"

    def __str__(self):
        return f"{self.id_card_number} -> {self.name}"

    def get_sex(self):
        if self.sex == "m":
            return "Male"
        else:
            return "Female"
        
class Admission(models.Model):
    id = models.AutoField(primary_key=True)
    adm_date = models.DateField(null=False)
    urgency = models.BooleanField(null=False)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)

    class Meta:
        db_table = "admission"

    def __str__(self):
        return f"{self.adm_date} - {self.patient}"


class Physician(models.Model):
    class SEX(models.TextChoices):
        FEMALe = "f"
        MALE = "m"

    speciality = models.ForeignKey(Speciality, on_delete=models.DO_NOTHING, null=False)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=False)
    id_card_number = models.CharField(
        primary_key=True,
        max_length=8,
        validators=[MinLengthValidator(8), MaxLengthValidator(8)],
    )
    healthcare_number = models.CharField(
        max_length=9,
        validators=[MinLengthValidator(9), MaxLengthValidator(9)],
        null=False,
        blank=False,
    )
    name = models.CharField(max_length=512, null=False)
    adress = models.CharField(max_length=512, blank=True, null=True)
    phone_number = models.CharField(max_length=9, blank=True, null=True)
    birth_date = models.DateField(null=False, blank=False)
    nationality = models.CharField(max_length=256, blank=True, null=True)
    sex = models.CharField(max_length=1, null=False, choices=SEX.choices, default="-")
    admissions = models.ManyToManyField(Admission)

    class Meta:
        db_table = "physician"

    def __str__(self):
        return f"{self.id_card_number} - Doctor {self.name}"
    
    def get_sex(self):
        if self.sex == "m":
            return "Male"
        else:
            return "Female"





# class PhysicianActions(models.Model):
#     admission = models.ForeignKey(Admission, models.DO_NOTHING)
#     physician = models.ForeignKey(Physician, models.DO_NOTHING)
#     action = models.TextField()

#     class Meta:
#         unique_together = (("admission", "physician"),)

#     def __str__(self):
#         return f" {self.physician} - {self.admission.patient.id_card_number} -> {self.action}"


class Diagnosis(models.Model):
    admission = models.ForeignKey(Admission, models.DO_NOTHING, null=False)
    physician = models.ForeignKey(Physician, models.DO_NOTHING, null=False)
    date = models.DateField(null=False, auto_now_add=True)
    diagnosis = models.ForeignKey(DiagnosisCode, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'diagnosis'
        unique_together = (("date", "diagnosis", "admission"),)

    def __str__(self):
        return f"Diagnosis {self.diagnosis} on {self.date} by {self.physician.name} related to Patient {self.admission.patient.id_card_number}"


class Exam(models.Model):
    admission = models.ForeignKey(Admission, models.DO_NOTHING, null=False)
    physician = models.ForeignKey(Physician, models.DO_NOTHING, null=False)
    prescription_date = models.DateField(null=False, auto_now_add=True)
    exam = models.ForeignKey(ExamsCode, models.DO_NOTHING, null=False)
    exam_date = models.DateField()
    result = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "exam"
        unique_together = (("admission", "exam_date", "exam"),)

    def __str__(self):
        return f"Exam {self.exam} for patient {self.admission.patient.id_card_number}"


class Prescription(models.Model):
    prescription_date = models.DateField(null=False, auto_now_add=True)
    admission = models.ForeignKey(Admission, models.DO_NOTHING, null=False)
    physician = models.ForeignKey(Physician, models.DO_NOTHING, null=False)

    class Meta:
        db_table = "prescription"

    def __str__(self):
        return f"{self.prescription_date} - {self.admission.patient.id_card_number} by {self.physician.id_card_number}"


class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(Prescription, models.DO_NOTHING)
    medication = models.ForeignKey(Medication, models.DO_NOTHING)
    dosage = models.CharField(max_length=512, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = (("medication", "prescription"),)

    def __str__(self):
        return f"{self.prescription} - {self.medication}"

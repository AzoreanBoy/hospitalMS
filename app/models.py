from django.db import models

# Domains
class Speciality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'speciality'
    
    def __str__(self):
        return self.name

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'department'
    
    def __str__(self):
        return self.name

class Medication(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'medication'
    
    def __str__(self):
        return self.name

class ExamsCode(models.Model):
    code = models.AutoField(primary_key=True)
    description = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'exams_code'
    
    def __str__(self):
        return self.description

class DiagnosisCode(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'diagnosis_code'
    
    def __str__(self):
        return self.description


# Relational Models
class Patient(models.Model):
    class SEX(models.TextChoices):
        FEMALe = "f"
        MALE = "m"
        
    
    person_id_card_number = models.BigIntegerField(primary_key=True)
    person_healthcare_number = models.IntegerField(blank=True, null=True)
    person_name = models.CharField(max_length=512, null=False)
    person_adress = models.CharField(max_length=512, blank=True, null=True)
    person_phone_number = models.CharField(max_length=9, blank=True, null=False)
    person_birth_date = models.DateField(null=False)
    person_nacionality = models.CharField(max_length=50, blank=True, null=True)
    person_sex = models.CharField(max_length=1, null=False, choices=SEX.choices, default = '-')

    class Meta:
        managed = False
        db_table = 'patient'
    
    def __str__(self):
        return f"{self.person_id_card_number} -> {self.person_name}"

class Physician(models.Model):
    class SEX(models.TextChoices):
        FEMALe = "f"
        MALE = "m"
    
    speciality = models.ForeignKey(Speciality, on_delete=models.DO_NOTHING, null=False)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, null=False)
    person_id_card_number = models.BigIntegerField(primary_key=True)
    person_healthcare_number = models.IntegerField(blank=True, null=True)
    person_name = models.CharField(max_length=512, null=False)
    person_adress = models.CharField(max_length=512, blank=True, null=True)
    person_phone_number = models.CharField(max_length=9, blank=True, null=True)
    person_birth_date = models.DateField(null=False)
    person_nacionality = models.CharField(max_length=50, blank=True, null=True)
    person_sex = models.CharField(max_length=1, choices=SEX.choices, default='-')

    class Meta:
        managed = False
        db_table = 'physician'
    
    def __str__(self):
        return f"{self.person_id_card_number} - Doctor {self.person_name}"

class Admission(models.Model):
    id =  models.AutoField(primary_key=True)
    adm_date = models.DateField(null=False)
    urgency = models.BooleanField()
    patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patient_person_id_card_number')

    class Meta:
        managed = False
        db_table = 'admission'
    
    def __str__(self):
        return f"{self.adm_date} - {self.patient}"

class AdmissionPhysician(models.Model):
    admission = models.ForeignKey(Admission, models.DO_NOTHING)
    physician = models.ForeignKey(Physician, models.DO_NOTHING, db_column='physician_person_id_card_number')

    class Meta:
        managed = False
        db_table = 'admission_physician'
        unique_together = (('admission', 'physician'),)
    
    def __str__(self):
        return f" {self.admission} - {self.physician}"

class Diagnosis(models.Model):
    comment = models.TextField(blank=True, null=True)
    diagnosis_date = models.DateField(null=False, auto_now_add=True)
    diagnosis_code = models.ForeignKey(DiagnosisCode, models.DO_NOTHING)
    admission = models.ForeignKey(Admission, models.DO_NOTHING)
    physician = models.ForeignKey(Physician, models.DO_NOTHING, db_column='physician_person_id_card_number')

    class Meta:
        managed = False
        db_table = 'diagnosis'
        unique_together = (('diagnosis_date', 'diagnosis_code', 'admission'),)
    
    def __str__(self):
        return f"Admission {self.diagnosis} of {self.diagnosis_date} by {self.physician}"

class Exam(models.Model):
    prescription_date = models.DateField(null=False, auto_now_add=True)
    exam_date = models.DateField()
    result = models.TextField(blank=True, null=True)
    exams_code = models.ForeignKey(ExamsCode, models.DO_NOTHING, db_column='exams_code_code')
    physician = models.ForeignKey(Physician, models.DO_NOTHING, db_column='physician_person_id_card_number')
    admission = models.ForeignKey(Admission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'exam'
        unique_together = (('exam_date', 'exams_code'),)
    
    def __str__(self):
        return f"Exam {self.exams_code} of {self.prescription_date} for admission {self.admission}"

class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    prescription_date = models.DateField(null=False, auto_now_add=True)
    admission = models.ForeignKey(Admission, models.DO_NOTHING, null=False)

    class Meta:
        managed = False
        db_table = 'prescription'
    
    def __str__(self):
        return f"{self.prescription_date} - {self.admission}"

class PrescriptionMedication(models.Model):
    dosage = models.CharField(max_length=512, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    medication_code = models.OneToOneField(Medication, models.DO_NOTHING, db_column='medication_code')
    prescription = models.ForeignKey(Prescription, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prescription_medication'
        unique_together = (('medication_code', 'prescription'),)
    
    def __str__(self):
        return f"{self.prescription} - {self.medication_code}"

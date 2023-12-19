from django.contrib import admin

from .models import *

# Domains Models 
admin.site.register(Speciality)
admin.site.register(Department)
admin.site.register(ExamsCode)

# Realtional Models
admin.site.register(Patient)
admin.site.register(Physician)
admin.site.register(Admission)
admin.site.register(Diagnosis)
admin.site.register(Exam)
admin.site.register(Prescription)
admin.site.register(PrescriptionMedication)

from django import forms

from .models import Patient, Admission


class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "id_card_number", "healthcare_number", "adress", "phone_number", "nationality", ]

    def __init__(self, *args, **kwargs):
        super(NewPatientForm, self).__init__(*args, **kwargs)
        self.use_required_attribute = False
        self.fields["name"].widget.attrs.update({
            "class": "shadow appearance-none border-2 rounded-lg py-2 px-3 w-full leading-tight focus:outline-none focus:shadow-outline",
            "placeholder": "Ex. Pedro Henrique ...", "id":"patient_name"})

        self.fields["id_card_number"].widget.attrs.update({
            "class": "shadow appearance-none border-2 rounded-lg py-2 px-3 leading-tight focus:outline-none focus:shadow-outline",
            "placeholder": "Ex. 123456789", "id":"patient_id_card_number" })
        self.fields["healthcare_number"].widget.attrs.update({
            "class": "shadow appearance-none border-2 rounded-lg py-2 px-3 leading-tight focus:outline-none focus:shadow-outline",
            "placeholder": "Ex. 132457689", "id":"patient_healthcare_number" })

        self.fields["adress"].widget.attrs.update({
            "class": "shadow appearance-none border-2 rounded-lg py-2 px-3 leading-tight focus:outline-none focus:shawdow-outline",
            "placeholder": "Ex. Coimbra", "id":"patient_address" })

        self.fields["nationality"].widget.attrs.update(
            {"class": "appearance-none shadow border-2 rounded-lg py-2 px-3 leading-tight",
             "placeholder": "Ex. Portuguese", "id":"patient_nationality" })

        self.fields["phone_number"].widget.attrs.update(
            {"class": "appearance-none shadow border-2 rounded-lg py-2 px-3 leading-tight",
             'placeholder': "Ex. 911111111","id":"patient_phone"})


class NewAdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ["urgency", "patient"]

    def __init__(self, *args, **kwargs):
        super(NewAdmissionForm, self).__init__(*args, **kwargs)
        self.use_required_attribute = False
        self.fields["urgency"].widget.attrs.update(
            {"class": "appearance-none shadow border-2 rounded-lg py-2 px-3 focus:outline-none"})
        self.fields["patient"].widget.attrs.update(
            {"class": "appearance-none shadow border-2 rounded-md py-2",},)
        self.fields["patient"].required = False
from django import forms

from .models import Patient


class NewPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "person_name",
            "person_id_card_number",
            "person_healthcare_number",
            "person_adress",
            "person_phone_number",
            "person_nacionality",
        ]

    def __init__(self, *args, **kwargs):
        super(NewPatientForm, self).__init__(*args, **kwargs)
        self.fields["person_name"].widget.attrs.update(
            {
                "class": "shadow appearance-none border-white border-2 rounded-lg py-2 px-3 w-full leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Ex. Pedro Henrique ...",
            }
        )

        self.fields["person_id_card_number"].widget.attrs.update(
            {
                "class": "shadow appearance-none border-white border-2 rounded-lg py-2 px-3 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Ex. 123456789",
            }
        )
        self.fields["person_healthcare_number"].widget.attrs.update(
            {
                "class": "shadow appearance-none border-2 rounded-lg py-2 px-3 leading-tight focus:outline-none focus:shadow-outline",
                "placeholder": "Ex. 132457689",
            }
        )

        self.fields["person_adress"].widget.attrs.update(
            {
                "class": "shadow appearance-none border-2 rounded-lg py-2 px-3 leading-tight focus:outline-none focus:shawdow-outline",
                "placeholder": "Ex. Coimbra",
            }
        )

        self.fields["person_nacionality"].widget.attrs.update(
            {
                "class": "appearance-none shadow border-2 rounded-lg py-2 px-3 leading-tight",
                "placeholder": "Ex. Portuguese",
            }
        )

        self.fields["person_phone_number"].widget.attrs.update(
            {"class": "appearance-none shadow border-2 rounded-lg py-2 px-3 leading-tight",
             'placeholder':"Ex. 911111111"}
        )

from django import forms


class SubcriptionForm(forms.Form):
    email_address = forms.EmailField(required=False, label='')

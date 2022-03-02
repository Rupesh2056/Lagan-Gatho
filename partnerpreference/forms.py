from django.forms import ModelForm
from .models import Preference
from django import forms
from userprofile.models import UserProfile 

class partner_preference_form(ModelForm):

    class Meta:
        model = Preference
        fields = ['marital_status']

    def __init__(self, *args, **kwargs):
        super(partner_preference_form, self).__init__(*args, **kwargs)
        self.fields['marital_status'].widget = forms.CheckboxSelectMultiple(choices=UserProfile.marital_status_choices)

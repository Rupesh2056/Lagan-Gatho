from django.shortcuts import render
from django.views.generic import CreateView
from .models import Preference
from .forms import partner_preference_form
# Create your views here.

class PreferenceSetupView(CreateView):
    model = Preference
    template_name = "partnerpreference/preference_setup.html"
    form_class = partner_preference_form
    success_url = '/'


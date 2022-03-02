from django.urls import path
from . import views

app_name= "partner_preference"
urlpatterns = [
    path('setup/',views.PreferenceSetupView.as_view(),name="preference_setup")
]

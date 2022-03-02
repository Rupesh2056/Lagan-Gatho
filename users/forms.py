from dataclasses import fields
from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):

    contact = forms.CharField(max_length = 10)
    GENDER_CHOICES= (
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    first_name = forms.CharField(max_length = 25)
    last_name = forms.CharField(max_length = 25)

    
    field_order = ['email','username','first_name','last_name','gender','contact','password1','password2']

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
       
        user = super(CustomSignupForm, self).save(request)

        # Add your own processing here.
        form = CustomSignupForm(request.POST)
        user.gender = self.cleaned_data['gender']
        user.contact = self.cleaned_data['contact']
        user.save()

        


        # You must return the original result.
        return user
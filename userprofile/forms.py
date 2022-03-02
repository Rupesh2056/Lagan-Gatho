from django.forms import ModelForm
from .models import UserProfile

class ProfileEditForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age','marital_status','DOB','religion','location','family_type','Rashi','education']
    


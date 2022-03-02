from django.shortcuts import render
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from userprofile.decorators import profile_setup_only


# Create your views here.
@login_required
@profile_setup_only

def index(request):
    allusers=CustomUser.objects.exclude(username=request.user.username)
    return render(request,'home/index.html',{'all_profiles':allusers});
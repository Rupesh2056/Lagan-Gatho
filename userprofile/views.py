from logging import raiseExceptions
from django.shortcuts import render
from .models import UserProfile
from django.shortcuts import get_object_or_404
from userconnectio.models import ConnectionRequest,ConnectionList
from django.views.generic import  CreateView
from userprofile.models import UserProfile

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from .decorators import profile_setup_only
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from .forms import ProfileEditForm
from django.contrib.auth.mixins import UserPassesTestMixin,AccessMixin
# Create your views here.

@profile_setup_only
@login_required
def ProfileView(request,id):
    print(id)
    profile = get_object_or_404(UserProfile,id=id)
    print("here")
    print(id)
    context = {}
    context['profile']=profile

    if request.user.userr.id == id:
        context['is_self']= True
    else:
        
            # check if the profile is a connection
            connectionlist_myconnection = ConnectionList.objects.get(user=request.user)
            if connectionlist_myconnection.is_connection(profile.user):
                context['is_connection']=True
            else:
                context['is_connection']=False
            #check if connection request is sent to the profile
            # print("upto here okay")
            requestlist_reqsent = ConnectionRequest.check_request(sender=request.user,receiver=profile.user)
            requestlist_reqreceived = ConnectionRequest.check_request(sender=profile.user,receiver=request.user)
            # print("here")
            print(requestlist_reqsent)
            print(requestlist_reqreceived)
            if requestlist_reqsent:
                context['request_sent']=True

            elif (requestlist_reqreceived):
                context['request_received']=True
            else:
                context['request_sent']=False
                context['request_received']=False
                context['no_requesst_sent_received']=True
    return render(request,'userprofile/index.html',context)

class ProfileCreateView(CreateView):

    model = UserProfile
    template_name='userprofile/profile_setup.html'
    fields = ['age','marital_status','DOB','religion','location','family_type','Rashi','education']

    success_url = '/'
    # form_class = ProfileCreationForm

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get(self, request):
        """Handle GET requests: instantiate a blank version of the form."""
        print("wtf")
        # self.object = self.get_object()
        try:
            
            profile = UserProfile.objects.get(user=request.user)
            if profile:
                raise Http404("opps something went wrong!");
        except ObjectDoesNotExist:
            return render(request,'userprofile/profile_setup.html',{'form':self.get_form})

        
class ProfileEditView(UserPassesTestMixin,UpdateView):
    model = UserProfile
    form_class = ProfileEditForm
    template_name = 'userprofile/edit_profile.html'
    success_url = '/'

    def test_func(self):
        profile =self.get_object()
        if profile.id==self.request.user.id:
            return True
        return False








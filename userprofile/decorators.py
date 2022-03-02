from functools import wraps
from django.http import HttpResponseRedirect
from .models import UserProfile
from django.core.exceptions import ObjectDoesNotExist

def profile_setup_only(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):
        try:
            profile= UserProfile.objects.get(user=request.user)
            return function(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/profile/profile_setup/')

  return wrap
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages



def unauthentticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request , 'Sorry You Can Not Login Or Register Again Before You Log Out ,, You Can Log Out From Above ...... ?')
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func
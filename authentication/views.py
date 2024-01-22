from django.shortcuts import render,redirect
from .forms import SignUpForm,ChangeInfo
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request,'home.html')


def signUp(request):
    if request.method=='POST':
       form = SignUpForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request,'Successfully Account created')
          return redirect('profile')
    else:
        form = SignUpForm()
    return render(request,'signUp.html',{'form':form,'type':'Sign Up'})

def LogIn(request):
     if request.method=='POST':
       form = AuthenticationForm(request=request,data=request.POST)
       if form.is_valid():
          name = form.cleaned_data['username']
          userPass = form.cleaned_data['password']
          user=authenticate(username=name,password=userPass)
          messages.success(request,'Logged In Successfully')
          
          if user is not None:
            login(request,user)
            return redirect('profile')

     else:
         form = AuthenticationForm()
     return render(request,'signUp.html',{'form':form,'type':'Login'})
    
@login_required(login_url='/login/')
def pass_Change(request):
     if request.method=='POST':
       form = PasswordChangeForm(user=request.user,data=request.POST)
       if form.is_valid():
          form.save()
          update_session_auth_hash(request,form.user)
          messages.success(request,'Successfully Change Password')
          return redirect('login')

     else:
        form = PasswordChangeForm(user=request.user)
     return render(request,'pass_change.html',{'form':form})

@login_required(login_url='/login/')
def profile(request):
    if request.method=='POST':
       form = ChangeInfo(request.POST, instance=request.user)
       if form.is_valid():
         form.save()
         messages.success(request,'Successfully Profile Update')
         return redirect('home')
    else:
        form = ChangeInfo(instance=request.user)
    return render(request,'profile.html',{'form':form})


@login_required(login_url='/login/')
def logOut(request):
    logout(request)
    messages.success(request,'Logged Out Successfully”')
    return redirect('home')
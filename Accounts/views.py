from django.shortcuts import render,redirect
from django.http import HttpResponse

from Vendor.forms import VendorForm
from . forms import UserForm
from .models import User,UserProfile
from django.contrib import messages
# Create your views here.
def Registeruser(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
        # create the user using the form for hashing the password
            # pass_hashing = form.cleaned_data['password']
            # u = form.save(commit=False)
            # u.set_password(pass_hashing)
            # u.role =User.CUSTOMER
            # u.save()
            # return redirect('Registeruser')

        # create the user using the create user method  for hashing the password
            first_hashing = form.cleaned_data['first_name']
            last_hashing = form.cleaned_data['last_name']
            username_hashing = form.cleaned_data['username']
            email_hashing = form.cleaned_data['email']
            password_hashing = form.cleaned_data['password']
            u = User.objects.create_user(first_name=first_hashing,last_name=last_hashing,
                                         username=username_hashing,email=email_hashing,
                                         password=password_hashing)
            u.role = User.CUSTOMER
            u.save()
            print("User created with hashing password successfully")
            messages.success(request,'Your account has been created succesfully!')
            return redirect('Registeruser')
        else:
            print('invalid form')
            print(form.errors)
    else:
        form = UserForm()
    context = {

        'form':form
    }
        

    return render(request,'accounts/register.html',context)

def Registervendor(request):
    
    if request.method == 'POST':
        # store the data and create the user
        u_form = UserForm(request.POST)
        v_form = VendorForm(request.POST,request.FILES)

        if u_form.is_valid() and v_form.is_valid():
            first_hashing = u_form.cleaned_data['first_name']
            last_hashing = u_form.cleaned_data['last_name']
            username_hashing = u_form.cleaned_data['username']
            email_hashing = u_form.cleaned_data['email']
            password_hashing = u_form.cleaned_data['password']
            ven_user = User.objects.create_user(first_name=first_hashing,last_name=last_hashing,
                                         username=username_hashing,email=email_hashing,
                                         password=password_hashing)
            print(ven_user)
            ven_user.role = User.RESTAURANT
            ven_user.save()
            # when this save is triggered it automatically created the userprofile  by signals
            vendor = v_form.save(commit=False)
            print(vendor)
            # Here before final save/commit the data vendor fileds such as vendor_name and vendor_license
            #  should be commited/saved ie some chnges should occured so vendor data is preserved in vendor
            vendor.user =ven_user
            # 'user' field in vendor assigned by ven_user ,which have created userdata
            ven_userprofile = UserProfile.objects.get(user=ven_user)
            # get 'user_profile' field in vendor from UserProfile model by assigning 'user' in UserProfile =  created ven_user just now
            vendor.user_profile = ven_userprofile
            vendor.save()
            # we are not manually give vendor_name and vendor_license to this becoz here v_form = VendorForm(request.POST,request.FILES)request.POST,request.FILES
            # taken careof
            messages.success(request,'Your vendor account has been created succesfully! Please wait for the approval')
            return redirect('Registervendor')

        else:
            print('invalid form')
            print(u_form.errors)

    else:
        u_form = UserForm()
        v_form = VendorForm()

    context = {
            'u_form':u_form,
            'v_form':v_form,
                  }
            
    return render(request,'accounts/registervendor.html',context)

   
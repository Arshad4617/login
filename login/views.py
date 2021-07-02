from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from . import models
# Create your views here.


@csrf_exempt
def home(request):
    usr_name = request.POST.get('name_field')
    usr_pass = request.POST.get('pass_field')
    sign_details = models.Login.objects.create(name=usr_name, usr_password=usr_pass)
    context = {
        "sign_details": sign_details,
    }
    return render(request, 'base.html', context)


@csrf_exempt
def create_new(request):
    cr_usr_name = request.POST.get('in_name')
    cr_usr_pass = request.POST.get('in_psw')
    cr_usr_pass_re = request.POST.get('in_psw_re')
    created_obj = models.CreateUser.objects.create(user_name=cr_usr_name, password=cr_usr_pass, re_password=cr_usr_pass_re)
    form_stuff = {
        'created_obj': created_obj,
    }
    return render(request, "pages/new_account.html", form_stuff,)


def forgot_pass(request):
    return render(request, "pages/forgot_pass.html")

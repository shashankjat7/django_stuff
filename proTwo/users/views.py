from django.shortcuts import render
from django.http import HttpResponse
from users.models import user
from . import forms
# Create your views here.


def home(request):
    return HttpResponse('this is home page')

def index(request):
    user_list=user.objects.order_by('age')
    users_dict = {
        'user_list': user_list
    }
    return render(request,'users/index.html',context=users_dict)


def signup_view(request):
    form = forms.signup_form()
    # if request.method == 'POST':
    #     form = forms.signup_form(request.POST)
    #
    #     if form.is_valid():
    #         user_detail = user.objects.get_or_create(name=form.cleaned_data['name'],
    #                                                  age=form.cleaned_data['age'],
    #                                                  email=form.cleaned_data['email'])[0]
    #         user_detail.save()

    if request.method == 'POST':
        form = forms.signup_form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('form is invalid')



    return render(request,'users/signup.html',{'form': form})

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    mydict = {
        'insert_me': "HI i am second page index"
    }
    return render(request,'second_app/index.html',context=mydict)


def help(request):
    help_dict = {
        'help_text': "I am here to help you"
    }
    return render(request, 'second_app/help.html', context=help_dict)
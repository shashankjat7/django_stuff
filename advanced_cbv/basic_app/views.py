# class based views

from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from . import models

# Create your views here.

class SchoolListView(ListView):
    # returns a predefined list as school_list and passes it in as context
    # we can define our own name as:
    context_object_name = 'schools'
    model = models.School
    # template_name = 'basic_app/school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    # usually returns the model name lower cased by default
    model = models.School
    template_name = 'basic_app/school_detail.html'




















# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CBV are cool')


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject'] = "Basic Injection"
        return context
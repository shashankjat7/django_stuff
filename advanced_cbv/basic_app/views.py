# class based views

from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

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


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
















# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CBV are cool')


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject'] = "Basic Injection"
        return context
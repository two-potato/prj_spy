from django.shortcuts import render
from django.views.generic import ListView, TemplateView


class TeletestView(TemplateView):
    template_name = "./index.html"

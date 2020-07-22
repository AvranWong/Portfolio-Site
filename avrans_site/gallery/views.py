from django.shortcuts import render
from django.views.generic import TemplateView,ListView,FormView
from gallery import forms
from gallery.forms import ContactForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = 'thankyou.html'

class PhotographyView(TemplateView):
    template_name = 'photography.html'

class ProgrammingView(TemplateView):
    template_name = 'programming.html'

class ThankYouView(TemplateView):
    template_name = 'thankyou.html'

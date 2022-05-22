from re import template
from django.shortcuts import render
from django.views import View
from academics.models import Academic
from experiences.models import Experience
from myprofile.models import MyProfile
from job_funcs.models import JobFunc
from contacts.models import Contact


class Index(View):
    template = 'index.html'

    def get(self, request):
        academics = Academic.objects.all()
        experiences = Experience.objects.all()
        myprofile = MyProfile.objects.all()
        job_funcs = JobFunc.objects.all()
        contacts = Contact.objects.all()

        return render(request, self.template, {'academics': academics, 'experiences': experiences, 'myprofile': myprofile, 'job_funcs': job_funcs, 'contacts': contacts})
from atexit import register
import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from minicrm.forms import *
from . import forms
from minicrm.models import *
from django.views.generic import ListView
from django.db.models import Sum, Avg

def minicrm(request):
    return render(request, "minicrm/minicrm.html")

def personal(request):
    return render(request, "minicrm/personal.html")

def add_artist(request):
    form = ArtistForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("minicrm")
    else:
        return render(request, "minicrm/add_artist.html", {"form": form})
    
def add_personal(request):
    form = PersonalForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            pproject = form.save(commit=False)
            pproject.log_date = datetime.now()
            pproject.save()
            return redirect("minicrm")
    else:
        return render(request, "minicrm/add_personal.html", {"form": form})
    
def add_project(request):
    form = ProjectForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            return redirect("minicrm")
    else:
        return render(request, "minicrm/add_project.html", {"form": form})
    
def edit_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("minicrm")
    else:
    
        return render(request, "minicrm/add_project.html", {"form": form})
    


class ArtistListView(ListView):
    model = Artist

    def get_context_data(self, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)
        return context
    
class PersonalProjectListView(ListView):
    model = PersonalProject

    def get_context_data(self, **kwargs):
        context = super(PersonalProjectListView, self).get_context_data(**kwargs)
        return context
    

def project_list(request):
    projects = Project.objects.all()
    artists = Artist.objects.all()
    pprojects = PersonalProject.objects.all()
    projects_count = Project.objects.count()
    projects_sum_count = Project.objects.aggregate(Sum('Price'))['Price__sum']
    projects_postp_count = Project.objects.aggregate(Sum('Postp'))['Postp__sum']
    projects_prep_count = Project.objects.aggregate(Sum('Prep'))['Prep__sum']
    ostatok = projects_sum_count - projects_prep_count
    avg_price = Project.objects.aggregate(Avg('Price'))['Price__avg']

    # projects_delta_count = projects_sum_count.value - projects_prep_count.value
    return render(request, 'minicrm/minicrm.html', {'projects': projects, 
                                                    'artists': artists, 
                                                    'pprojects': pprojects, 
                                                    'projects_count': projects_count,
                                                    'projects_prep_count': projects_prep_count,
                                                    'projects_sum_count': projects_sum_count,
                                                    'ostatok': ostatok,
                                                    'avg_price': avg_price,
                                                    'projects_postp_count': projects_postp_count,
                                                    })
    
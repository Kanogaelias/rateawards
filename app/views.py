from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project,Profile
from .forms import NewProjectForm,NewProfileForm,RateForm

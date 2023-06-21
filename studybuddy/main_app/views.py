from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .models import Study_Group, School, User, Profile, Topic
from django.urls import reverse
from django.http import HttpResponse
import datetime

# Create your views here.


def home(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def index(request):
    # school = School.objects.get(request.user.profile.school)
    my_groups = Study_Group.objects.filter(creator=request.user)
    all_groups = Study_Group.objects.filter(date__gt=datetime.date.today())
    return render(request, 'groups/index.html', {
        'my_groups': my_groups, 'all_groups': all_groups
    })


@login_required
def detail(request, group_id):
    study_group = Study_Group.objects.get(id=group_id)
    return render(request, 'groups/detail.html', {'study_group': study_group})


class CreateGroup(LoginRequiredMixin, CreateView):
    model = Study_Group
    fields = ('name', 'topic', 'date', 'time', 'description', 'location')
    # topics = Topic.objects.all().values_list('name')
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        user = User.objects.get(username=self.request.user)
        profile = Profile.objects.get(user=user)
        school = School.objects.get(id=profile.school.id)
        form.instance.school = school
        form.instance.creator = self.request.user
        if school.name == 'No School':
            return redirect(reverse('school_select'))
        return super().form_valid(form)


@login_required
def school_select(request):
    schools = School.objects.all().order_by('name')
    return render(request, 'main_app/school_select.html', {
        'schools': schools
    })


@login_required
def set_school(request, school_id):
    school = School.objects.get(id=school_id)
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)
    profile.school = school
    profile.save()
    return redirect('index')


class EditGroup(UpdateView):
    model = Study_Group
    fields = ['name', 'date', 'time', 'description', 'location', 'topic']
    success_url = '/'


class DeleteGroup(LoginRequiredMixin, DeleteView):
    model = Study_Group
    success_url = '/'

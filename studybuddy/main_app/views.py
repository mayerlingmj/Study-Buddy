from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Study_Group, School, User, Profile
from django.urls import reverse

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


def index(request):
    # school = School.objects.get(request.user.profile.school)
    my_groups = Study_Group.objects.filter(creator=request.user)
    all_school_groups = Study_Group.objects.filter(attending=request.user)
    return render(request, 'groups/index.html', {
        'my_groups': my_groups
    })


def detail(request, group_id):
    study_group = Study_Group.objects.get(id=group_id)
    return render(request, 'groups/detail.html', {'study_group': study_group})


class CreateGroup(CreateView):
    model = Study_Group
    fields = ['name', 'description', 'location', 'topic']
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


def school_select(request):
    schools = School.objects.all().order_by('name')
    return render(request, 'main_app/school_select.html', {
        'schools': schools
    })


def set_school(request, school_id):
    school = School.objects.get(id=school_id)
    user = User.objects.get(username=request.user)
    profile = Profile.objects.get(user=user)
    profile.school = school
    profile.save()
    return redirect('index')

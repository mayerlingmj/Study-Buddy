from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Study_Group, School, User, Profile

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
    return render(request, 'groups/index.html')


def detail(request):
    return render(request, 'groups/detail.html')


class CreateGroup(CreateView):
    model = Study_Group
    fields = ['name', 'description', 'location', 'topic']

    def form_valid(self, form):
        form.instance.user = self.request.user
        user = User.objects.get(username=self.request.user)
        profile = Profile.objects.get(user=user)
        school = School.objects.get(id=profile.school.id)
        form.instance.school = school
        return super().form_valid(form)


def school_select(request):
    schools = School.objects.all()
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

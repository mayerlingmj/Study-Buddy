from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Study_Group

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
    fields = ['location', 'topic', 'school']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def school_select(request):
    return render(request, 'main_app/school_select.html')

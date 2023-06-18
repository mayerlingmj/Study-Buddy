from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'homepage.html')

def about(request):
  return render(request, 'about.html')

def signup(request):
  return render(request, 'registration/signup.html')

def index(request):
  return render(request, 'groups/index.html')

def detail(request):
  return render(request, 'groups/detail.html')
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('school')
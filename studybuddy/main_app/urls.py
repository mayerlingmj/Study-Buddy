from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('study_groups/create/', views.CreateGroup.as_view(),
         name='study_groups_create'),
    path('school_select/', views.school_select, name='school_select'),
    path('school_select/<int:school_id>/', views.set_school, name='set_school'),
    path('groups/<int:group_id>/', views.detail, name='detail')
]

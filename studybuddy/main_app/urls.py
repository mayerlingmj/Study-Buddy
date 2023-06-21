from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('study_groups/create/', views.CreateGroup.as_view(),
         name='study_groups_create'),
    path('study_groups/<int:pk>/delete/', views.DeleteGroup.as_view(),
         name='study_groups_delete'),
    path('school_select/', views.school_select, name='school_select'),
    path('school_select/<int:school_id>/', views.set_school, name='set_school'),
    path('study_groups/<int:group_id>/', views.detail, name='detail'),
    path('study_groups/<int:pk>/edit',
         views.EditGroup.as_view(), name='study_groups_edit'),
    path('study_groups/<int:group_id>/attending',
         views.set_attending, name='set_attending'),
    path('topic/<int:topic_id>/', views.filter_by_topic, name='filter_by_topic')
]


from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from apps.academics import views


admin.autodiscover()
router = routers.DefaultRouter()

urlpatterns = [
    path('session', views.SessionListView.as_view(), name='sessions_list'),
    path('session/<int:id>/', views.SessionDetailView.as_view(),
         name='session_detail'),
    path('session/active/', views.ActiveSessionView.as_view(), name="active_session"),
    path('session/activate/<int:id>',
         views.ActivateSessionView.as_view(), name="activate_session"),


    path('level', views.LevelListView.as_view(), name="level_list"),
    path('level/<int:id>', views.LevelDetailView.as_view(), name="level_detail"),
    path('level/session/<int:id>',
         views.LevelBySessionView.as_view(), name="level_by_session"),


    path('section', views.SectionListView.as_view(), name="section_list"),
    path('section/<int:id>', views.SectionDetailView.as_view(),
         name="section_detail"),
    path('section/level/<int:id>',
         views.SectionByLevelView.as_view(), name="section_by_level"),


    path('class', views.ClassListView.as_view(), name="class_list"),
    path('class/section/<int:id>',
         views.ClassBySectionView.as_view(), name="class_by_section"),
    path('class/students/<int:id>', views.ClassStudentsView.as_view(), name="class_students"),
    path('class/subjects/<int:id>', views.ClassSubjectView.as_view(), name="class_subjects"),
    path('class/teacher/<int:id>',views.ClassTeacherView.as_view(), name="class_teachers"),

    path('classsubject', views.ClassSubjectListView.as_view()),


    path('subject', views.SubjectListView.as_view(), name="subject_list"),
    path('subject/<int:id>', views.SubjectDetailView.as_view(), name="subject_detail")
]

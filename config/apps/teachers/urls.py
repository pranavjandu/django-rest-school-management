from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from apps.teachers import views


admin.autodiscover()
router = routers.DefaultRouter()

urlpatterns = [
    path('api/',views.TeacherListView.as_view(),name='teachers_list'),
    path('api/<int:id>/',views.TeacherDetailView.as_view(),name='teacher_detail')

]

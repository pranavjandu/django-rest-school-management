
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from apps.students import views


admin.autodiscover()
router = routers.DefaultRouter()

urlpatterns = [
    path('api/',views.StudentListView.as_view(),name='students_list'),
    path('api/<int:id>/',views.StudentDetailView.as_view(),name='students_detail')

]

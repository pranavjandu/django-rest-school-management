from apps.academics.models import Class, Level, Section, Session, Subject
from django.contrib import admin

# Register your models here.

admin.site.register(Session)
admin.site.register(Level)
admin.site.register(Section)
admin.site.register(Class)
admin.site.register(Subject)
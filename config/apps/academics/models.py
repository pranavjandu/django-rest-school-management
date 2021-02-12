from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField
from apps.teachers.models import Teacher
from apps.students.models import Students


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    order_number = models.PositiveIntegerField(null=True, blank=True)
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name="session")
    objects = models.Manager()

    def __str__(self):
        return self.name


class Section(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    order_number = models.PositiveIntegerField(null=True, blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    order_number = models.PositiveIntegerField(null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    students = models.ManyToManyField(
        Students, null=True, blank=True, related_name="classofstudent")
    objects = models.Manager()

    def __str__(self):
        return self.name


class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    external_subject_id = models.PositiveIntegerField(null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class ClassSubject(models.Model):
    id = models.AutoField(primary_key=True)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="classsubject", null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="classsubject", null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, related_name="classsubject", null=True)

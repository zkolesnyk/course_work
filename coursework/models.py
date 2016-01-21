# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    birthdate = models.DateField()
    phone_number = models.IntegerField(null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.surname, self.name)

    class Meta:
        ordering = ["name"]
        db_table = "student"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    # practice = models.Fie(Lecturer, blank=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        db_table = "subject"
        ordering = ["name"]


class Number(models.Model):
    number = models.PositiveIntegerField()

    def __unicode__(self):
        return "%d" % self.number

    class Meta:
        db_table = "number"


class Lecturer(models.Model):
    fullname = models.CharField(max_length=100)
    subjects = models.ManyToManyField(Subject, blank=True)

    def __unicode__(self):
        return "%s" % self.fullname

    class Meta:
        db_table = "lecturer"
        ordering = ["fullname"]


class Weekday(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s" % self.name


class Pair(models.Model):
    first_week = models.BooleanField()
    subject = models.ForeignKey(Subject, null=True, blank=True)
    weekday = models.ForeignKey(Weekday, null=True)
    lecturer = models.ForeignKey(Lecturer, null=True, blank=True)
    number = models.ForeignKey(Number, null=True)

    def __unicode__(self):
        if self.first_week:
            week = "I тиждень"
        else:
            week = "II тиждень"
        if self.subject is not None:
            if self.lecturer is None:
                return "%s %s %s пара - %s" % (week, self.weekday, self.number, self.subject)
            else:
                return "%s %s %s пара - %s Викладач: %s" % (week, self.weekday, self.number, self.subject, self.lecturer)
        return "%s %s %s пара - немає" % (week, self.weekday, self.number)

    class Meta:
        db_table = "pairs"
        ordering = ["-first_week", "weekday", "number"]


class StudyMaterial(models.Model):
    name = models.TextField(blank=True)
    comment = models.TextField(blank=True)
    author = models.ForeignKey(User)
    file = models.FileField(null=True, blank=True, upload_to='')
    timestamp = models.TimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        db_table = "study materials"
        ordering = ['name']

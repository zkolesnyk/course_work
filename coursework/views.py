# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from coursework.models import *
from django.template.context_processors import csrf
from untitled1.settings import MEDIA_ROOT
from os import listdir


def home(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    return render_to_response('homepage.html', args)


@login_required(login_url='/auth/login/')
def group_list(request):
    students = Student.objects.all()
    return render_to_response('group_list.html', {'students': students, 'username': auth.get_user(request).username})


def login(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Користувач не знайдений"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
                                        password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('register.html', args)


@login_required(login_url='/auth/login/')
def schedule(request):
    args = {}
    args.update(csrf(request))
    args['pairs'] = Pair.objects.all()
    args['weekdays'] = Weekday.objects.all().reverse()
    return render_to_response('schedule.html', args)


def upload(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        q = request.POST
        if 'file' in request.FILES:
            upfile = request.FILES['file']
            material = StudyMaterial(name=q['name'], comment=q['comment'], author=request.user, file=upfile)
            material.save()
    objects = list(StudyMaterial.objects.all())[-20:]
    args['objects'] = objects
    return render_to_response('upload.html', args)


def study_materials(request):
    materials = StudyMaterial.objects.all()
    return render_to_response('study_materials.html',
                              {'materials': materials,
                               'total_files': listdir(MEDIA_ROOT),
                               'path': MEDIA_ROOT},
                              context_instance=RequestContext(request))
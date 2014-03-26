#!/usr/bin/env python

"""
views.py

Getting requests from users and forwarding them onto the appropriate page

"""

__author__      = "Arnas Binkauskas, Donald Martin, Josh McGhee & Irina Preda"
__copyright__   = "Copyright 2014, University of Glasgow, Team P"
__version__     = "1.0"
__status__      = "Development"

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from course.models import User, LessonCompletions
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.shortcuts import redirect, render_to_response

def totalPoints(user):
    lessons = LessonCompletions.objects.filter(user=user)
    points = 0
    
    for lesson in lessons:
        points += lesson.lesson.award
        
    return points

@login_required
def students(request):
	context = RequestContext(request)
	users   = User.objects.all()
	usrList = []
	details = {"users": usrList}
	
	for user in users:
	    info             = {}
	    info["forename"] = user.first_name
	    info["surname"]  = user.last_name
	    info["points"]   = totalPoints(user)
	    usrList.append(info)
	    
	return render_to_response('student/list.html', details, context)
	    

@login_required
def student_profile(request):
	user    = request.user
	lessons = LessonCompletions.objects.filter(user=user)
	titles  = []
	points  = 0
	
	for lesson in lessons:
	    titles.append(lesson.lesson.title)
	    points += lesson.lesson.award
	
	context       = RequestContext(request)
	details       = {"user": user, "points": points, "lessons":titles}    
	template      = loader.get_template('student/profile.html')
	authenticater = request.user.is_authenticated()
	
	print(user.first_name)
	print(titles)
	return render_to_response('student/profile.html', details, context)

@login_required
def logout_user(request):
    logout(request)
    return redirect("lessons")

@login_required
def delete_user(request):
    request.user.delete()
    return redirect("lessons")

@login_required
def edit_profile(request):
    user = request.user
    context = RequestContext(request)
    details = {}

    if request.method == 'POST':
        user.first_name = request.POST["newfirstname"]
        user.last_name = request.POST["newlastname"]
        user.email = request.POST["newemail"]
        user.save()
        details = {"user": user, "done" : True}

    template = loader.get_template('student/edit_profile.html')
    return render_to_response('student/edit_profile.html', details, context)
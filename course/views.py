#!/usr/bin/env python

"""
views.py

Getting requests from users and forwarding them onto the appropriate page

"""
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext, loader
from course.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout, authenticate
from django.shortcuts import redirect, render_to_response

def index(request):
    context = RequestContext(request)
    details = {"failedLogin": False, "inactiveAccount": False}
    
    if request.user.is_authenticated():
        return HttpResponseRedirect("/brainstorm")
    else:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user     = authenticate(username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect("/brainstorm")
                else:
                    details["inactiveAccount"] = True
                    return render_to_response("course/index.html", details, context)  
            else:
                print("Failing")
                details["failedLogin"] = True
                return render_to_response("course/index.html", details, context)
        else:
            return render_to_response("course/index.html", details, context)  
            
        return render_to_response("course/index.html", details, context)

def register_individual(request):
    context = RequestContext(request)
    details = {"alreadyExists": False, "complete": False}
    
    registered = False
    
    if request.method == "POST":
        uname = request.POST["email"]
        fname = request.POST["forename"]
        sname = request.POST["surname"]
        email = request.POST["email"]
        pword = request.POST["password"]
        
        if User.objects.filter(email=email).count():
            details["alreadyExists"] = True
        else:
            user  = User.objects.create_user(email, email, pword)
            user.first_name = fname
            user.last_name  = sname
            user.save()
            
            details["complete"] = True
    
    return render_to_response("course/register-individual.html", details, context)

def register_employee(request):
    context = RequestContext(request)
    return render_to_response("course/register-employee.html", {}, context)

# List of Lessons --------------------------------------------------------------
#
# Check that a user is logged in & display the webpage of lessons

def brainstorm(request):	
    context = RequestContext(request)
    details = {"failedLogin": False, "inactiveAccount": False}
    return render_to_response("course/brainstorm.html", details, context)

def tutorial(request):    
    context = RequestContext(request)
    details = {"failedLogin": False, "inactiveAccount": False}
    return render_to_response("course/tutorial.html", details, context)

@login_required
def lessons(request):
	allLessons      = Lesson.objects.all()
	completions     = LessonCompletions.objects.filter(user=request.user)
	
	completedLessons = []
	
	for completion in completions:
	    completedLessons.append(completion.lesson.title)
	    
	template        = loader.get_template('course/brainstorm2.html')
	authenticater   = request.user.is_authenticated()
	
	context         = RequestContext(request,
	                                    {'lessons': allLessons,
	                                     'authenticated':authenticater,
	                                     'completed': completedLessons,
	                                })
	
	return HttpResponse(template.render(context))


# Lesson Page ------------------------------------------------------------------
#
# Check that user is logged in & forward to that lesson's page

@login_required
def lesson_page(request):
    if request.method == "POST":
        lesson = Lesson.objects.get(title = request.POST["title"])
        LessonCompletions.objects.get_or_create(user=request.user, lesson=lesson)
        return lessons(request)
    else:
        lesson          = Lesson.objects.get(title = request.GET.get("title", "NULL"))
        template        = loader.get_template('course/lessonpage.html')
        authenticater   = request.user.is_authenticated()
        
        context         = RequestContext(request, {'resources':lesson,
                                                   'authenticated':authenticater,
                                                   'courseID':request.GET.get("title", "NULL"),})
        
        return HttpResponse(template.render(context))
    
# Logout User ------------------------------------------------------------------
#
# Check that user is logged in & log them out from the system

@login_required
def logout_user(request):
    logout(request)
    return redirect("/")

@login_required
def delete_user(request):
    request.user.delete()
    return redirect("/")

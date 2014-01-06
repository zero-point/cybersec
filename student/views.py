from django.http import HttpResponse
from django.template import RequestContext, loader
from course.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.shortcuts import redirect

@login_required
def students(request):
	allStudents     = Student.objects.all()
	template        = loader.get_template('student/list.html')
	authenticater   = request.user.is_authenticated()
	context         = RequestContext(request, {'students': allStudents,'authenticated':authenticater,})
    
	return HttpResponse(template.render(context))

@login_required
def student_profile(request):
	allRelevantRes  = Student.objects.filter(id = 0)
	template        = loader.get_template('student/profile.html')
	authenticater   = request.user.is_authenticated()
	context         = RequestContext(request, {'res': allRelevantRes, 'authenticated':authenticater,})
	
	return HttpResponse(template.render(context))

@login_required
def logout_user(request):
    logout(request)
    return redirect("lessons")
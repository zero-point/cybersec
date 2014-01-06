from django.conf.urls import patterns, url


from student import views

urlpatterns = patterns('',
    url(r'^$', views.students, name='students'),
    url(r'^student_profile/$', views.student_profile, name='student_profile'),
)     
from django.conf.urls import patterns, url


from course import views

urlpatterns = patterns('',
    url(r'^$', views.lessons, name='lessons'),
    url(r'^logout/', views.logout_user, name='logout'),
    url(r'^delete/', views.delete_user, name='delete'),
    url(r'^login/', 'django.contrib.auth.views.login', {'template_name': 'course/login.html'}),
    url(r'^res/', views.lesson_page),

)     

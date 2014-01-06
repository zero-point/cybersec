from django.contrib import admin
from course.models import Lesson, Student, WebResource, PictureResource, VideoResource, CodeResource, DemoResource

# Register your models here.
admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(WebResource)
admin.site.register(PictureResource)
admin.site.register(VideoResource)
admin.site.register(CodeResource)
admin.site.register(DemoResource)
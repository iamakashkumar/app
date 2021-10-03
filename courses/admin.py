from django.contrib import admin
from courses.models import Course, Tags, Prerequisite, Learning , Video
# Register your models here.

class TagsAdmin(admin.TabularInline):
    model=Tags

class VideoAdmin(admin.TabularInline):
    model=Video

class PrerequisiteAdmin(admin.TabularInline):
    model=Prerequisite

class LearningAdmin(admin.TabularInline):
    model=Learning

class CourseAdmin(admin.ModelAdmin):
    inlines = [TagsAdmin, LearningAdmin, PrerequisiteAdmin, VideoAdmin]

admin.site.register(Course, CourseAdmin)
admin.site.register(Video)



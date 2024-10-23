
from django.contrib import admin
from .models import Faculty, Parent, Profile, Teacher, Attendance, Student

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student', 'user')
    search_fields = ('name', 'student__first_name', 'user__username')
    raw_id_fields = ('student', 'user')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)
    raw_id_fields = ('user',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user', 'faculty')
    search_fields = ('first_name', 'last_name', 'user__username')
    list_filter = ('faculty',)
    raw_id_fields = ('user', 'profile')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'time', 'status', 'duration_hours')
    list_filter = ('date', 'status')
    search_fields = ('user__username',)
    date_hierarchy = 'date'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user', 'faculty', 'status')
    list_filter = ('faculty', 'status')
    search_fields = ('first_name', 'last_name', 'user__username')
    raw_id_fields = ('user', 'profile')

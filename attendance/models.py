from django.db import models
from django.contrib.auth.models import User
from .subject_models import Subject

class Faculty(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name

class Parent(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    name = models.CharField(max_length=300)  # Fixed typo here
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to='profile_photos')
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    first_name = models.CharField(max_length=300, default="Unknown")
    last_name = models.CharField(max_length=300, default="Unknown")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='teachers')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    duration_hours = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=[
        ('present', 'Present'),
        ('late', 'Late'),
        ('absent', 'Absent')
    ])

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'Attendances'

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.status}"

class Student(models.Model):
    first_name = models.CharField(max_length=300, default="Unknown")
    last_name = models.CharField(max_length=300, default="Unknown")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='students')
    latitude = models.FloatField(default=0.0, null=True, blank=True)
    longitude = models.FloatField(default=0.0, null=True, blank=True)
    status = models.CharField(max_length=30, choices=[
        ('present', 'Present'), 
        ('absent', 'Absent'), 
        ('late', 'Late')
    ], blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    check_in_time = models.TimeField(null=True, blank=True)

    def get_attendance_streak(self):
        attendance_records = Attendance.objects.filter(user=self.user).order_by('-date')
        streak = 0
        for record in attendance_records:
            if record.status == 'present':
                streak += 1
            
            else:
                break
        return streak

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
from django.contrib import admin
from .models import WeeklyDanceClass, Level, CourseReview, DanceStyle

# Register your models here.
admin.site.register(WeeklyDanceClass)
admin.site.register(DanceStyle)
admin.site.register(Level)
admin.site.register(CourseReview)
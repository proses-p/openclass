from django.contrib import admin
from .models import Resource
from .models import University
from .models import Course
from .models import Semester
from .models import Faculty

# Register your models here.
admin.site.register(Resource)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Semester)
admin.site.register(Faculty)
from django.db import models

# Create your models here.
# university model
class University(models.Model):
    name = models.CharField(max_length=190)
    location = models.CharField(max_length=100)
    def __str__(self):
            return self.name
    
# courses models
class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=100)
    def __str__(self):
          return f"{self.name} - {self.university.name if self.university else 'No University'}"

# faculty models
class Faculty(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='faculties', null=True)
    name = models.CharField(max_length=100, null=True)
    def __str__(self):
        return f"{self.name} ({self.university.name})"

# semester models
class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='semesters')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        course_name = self.course.name if self.course else "No Course"
        return f"{self.name} ({self.course.name})"

# resource models   
class Resource(models.Model):
    LEVEL_CHOICES = [
        ('degree1', 'degree year 1'),
        ('degree2', 'degree year 2'),
        ('degree3', 'degree year 3'),
        ('degree4', 'degree year 4'),
        ('diploma1', 'diploma year 1'),
        ('diploma2', 'diploma year 2'),
        ]
    CATEGORY_CHOICES = [
        ('pastpaper', 'Past Paper'),
        ('notes', 'Notes&Slides'),
        ('book', 'Books'),
        ]
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='resources', null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='faculties', null=True)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True)
    level = models.CharField(max_length=100, choices=LEVEL_CHOICES, null=True)
    category = models.CharField(max_length=18, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        if self.semester:
           return f"{self.title} - {self.semester.name}"
        return self.title

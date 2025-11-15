from django.shortcuts import render, get_object_or_404
from .models import Resource, University, Course, Semester, Faculty

# Create your views here.
def home(request):
    return render(request, "resources/index.html")
# rendering resources from the database and showing them to the templates for pastpapers
def pastpaper_level(request, level, faculty_id):
        faculty = get_object_or_404(Faculty, id=faculty_id)
        resources = Resource.objects.filter(category="pastpaper", level=level, faculty=faculty)
        return render(request, 'resources/resource_list.html', {'resources': resources, 'faculty': faculty, 'title': f"Past Papers - {level}" })
        
# fatches due to the level
def pastpaper(request):
    levels = [
        ('degree1', 'degree year 1'),
        ('degree2', 'degree year 2'),
        ('degree3', 'degree year 3'),
        ('degree4', 'degree year 4'),
        ('diploma1', 'diploma year 1'),
        ('diploma2', 'diploma year 2'),
        ]
    return render(request, 'resources/pastpaper.html', {'levels': levels})

# view to fetch universities in database
def select_university(request, level):
    universities = University.objects.all()
    return render(request, 'resources/select_university.html', {'universities': universities, 'level': level})
    
# view to fetch faculty from the database
def select_faculty(request, level, university_id):
    university = get_object_or_404(University, id=university_id)
    faculties = Faculty.objects.filter(university=university).distinct()
    return render(request, 'resources/select_faculty.html', {'faculties': faculties, 'university': university, 'level': level})

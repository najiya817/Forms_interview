from django.shortcuts import render
from .models import Student
from .forms import CourseForm
from django.forms import formset_factory


def NewPage(request, student_id=1):
    CourseFormSet = formset_factory(CourseForm, extra=1)
    student = Student.objects.get(id=student_id)

    if request.method == 'POST':
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return render(request, 'student_not_found.html', {'student_id': student_id})

        formset = CourseFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    course = form.save(commit=False)
                    course.student = student
                    course.save()
    else:
        formset = CourseFormSet()

    return render(request, 'newpage.html', {'student': student, 'formset': formset})

from django.shortcuts import redirect, render
from django import views
from .models import *
from .forms import *
from .forms import *

def Home(request):
    if request.method == "POST":
        registerform = RegisterForm(request.POST)
        formset = CourseModelFormset(request.POST, queryset=Courses.objects.none())

        if registerform.is_valid() and formset.is_valid():
            register = registerform.save()
            for form in formset:
                if form.is_valid() and form.cleaned_data:
                    degree = form.cleaned_data["degree"]
                    university = form.cleaned_data["university"]
                    year = form.cleaned_data["year"]
                    course = Courses(
                        course_id=register, degree=degree, university=university, year=year
                    )
                    course.save()
            return redirect("home")
        else:
            print("Register Form Errors:", registerform.errors)
            print("Formset Errors:", formset.errors)
    else:
        registerform = RegisterForm()
        formset = CourseModelFormset(queryset=Courses.objects.none())
        print(formset.data)

    return render(
        request,
        "home.html",
        {
            "registerform": registerform,
            "formset": formset,
        },
    )





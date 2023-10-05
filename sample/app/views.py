from django.shortcuts import redirect, render
from django import views
from .models import *
from .forms import *
from .forms import *


def Home(request):
    if request.method == "POST":
        registerform = RegisterForm(request.POST)
        formset = CourseModelFormset(
            request.POST, queryset=Courses.objects.none()
        )

        if registerform.is_valid() and formset.is_valid():
            register = registerform.save()
            print(register)
            for form in formset:
                if form.cleaned_data:
                    degree = form.cleaned_data["degree"]
                    university = form.cleaned_data["university"]
                    year = form.cleaned_data["year"]
                    print(degree)
                    course = Courses.objects.create(
                        course_id=register, degree=degree, university=university, year=year
                    )
                    course.save()
                    return redirect("home")
    else:
        registerform = RegisterForm()
        formset = CourseModelFormset(queryset=Courses.objects.none())
        print(formset.data)

    return render(
        request,
        "home1.html",
        {
            "registerform": registerform,
            "formset": formset,
        },
    )



# def Home(request):
#     if request.method == "POST":
#         register_formset = RegisterForm(request.POST)
#         course_formset = CourseModelFormset(request.POST,queryset=Courses.objects.none())

#         if register_formset.is_valid() and course_formset.is_valid():
#             register_formset.save()
#             # register_instances = []
#             for form in course_formset:
#                 if form.cleaned_data:
#                     degree=form.cleaned_data['degree']
#                     university=form.cleaned_data['university']
#                     year=form.cleaned_data['year']
#                     # register_instance = register_form.save()
#                     # register_instances.append(register_instance)
#                     # print("Register Instances:", register_instances)
#                     courses=Courses.objects.create(degree=degree,university=university,year=year)
#                     courses.save()
#             # for register_instance, course_form in zip(register_instances, course_formset.forms):
#             #     if course_form.cleaned_data:
#             #         course_instance = course_form.save(commit=False)
#             #         course_instance.course_id = register_instance
#             #         course_instance.save()

#             return redirect('home')

#     else:
#         register_formset = RegisterForm()
#         course_formset = CourseModelFormset()
#         print(course_formset.data)
#     return render(
#         request,
#         "home.html",
#         {
#             "register_formset": register_formset,
#             "course_formset": course_formset,
#         },
#     )


# def Home(request):
#     template_name = 'home.html'
#     if request.method == 'GET':
#         registerform = RegisterModelFormset(request.GET or None)
#         courseform = CourseModelFormset(queryset=Courses.objects.none())
#     elif request.method == 'POST':
#         registerform = RegisterModelFormset(request.POST)
#         courseform = CourseModelFormset(request.POST)
#         if registerform.is_valid() and courseform.is_valid():
#             # first save this book, as its reference will be used in `Author`
#             register = registerform.save()
#             for form in courseform:
#                 if form.cleaned_data:
#                     degree=form.cleaned_data['degree']
#                     university=form.cleaned_data['university']
#                     year=form.cleaned_data['year']
#                     Courses.objects.create(degree=degree,university=university,year=year).save()
#                 # so that `book` instance can be attached.
#                     # course = form.save(commit=False)
#                     # course.register = course
#                     # course.save()
#             return redirect('home')
#     else:
#             registerform = RegisterModelFormset()
#             courseform = CourseModelFormset(queryset=Courses.objects.none())

#     return render(request, template_name, {
#         'registerform': registerform,
#         'courseform': courseform,
#     })


# Create your views here.
# def Home(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         course_id = request.POST.get("course_id")
#         register = Register(reg_id=course_id, name=name, email=email)
#         register.save()

#         for i in range(0, 3):
#             degree = request.POST.get(f"degree_{i}")
#             university = request.POST.get(f"university_{i}")
#             year = request.POST.get(f"year_{i}")
#             print(degree)

#             if degree and university and year:
#                 course = Courses(
#                     course_id=register, degree=degree, university=university, year=year)
#                 course.save()

#     return render(request, "home.html")


# def Home(request,reg_id=70):
#     CourseFormset=formset_factory(CourseForm,extra=1)
#     register=Register.objects.get(id=reg_id)
#     if request.method=='POST':
#         try:
#             register=Register.objects.get(id=reg_id)
#         except Register.DoesNotExist:
#             return render(request, 'home.html', {'reg_id': reg_id})
#         formset=CourseFormset(request.POST)
#         if formset.is_valid():
#             for form in formset:
#                 if form.cleaned_data:
#                     course=form.save(commit=False)
#                     course.register=register
#                     course.save()
#     else:
#         formset=CourseFormset()
#     return render(request, 'home.html',{'register':register,'formset':formset})

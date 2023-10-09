from django.shortcuts import redirect, render
from django.views import View
from django.contrib import messages
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404


def MainHome(request):
    return render(request, "mainhome.html")


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
                    course = Courses.objects.create(
                        course_id=register,
                        degree=degree,
                        university=university,
                        year=year,
                    )
                    course.save()
            return redirect("mhome")
        else:
            print("Register Form Errors:", registerform.errors)
            print("Formset Errors:", formset.errors)
    else:
        registerform = RegisterForm()
        formset = CourseModelFormset(queryset=Courses.objects.none())
        print(formset.data)
    messages.success(request, "registration successful")

    return render(
        request,
        "home.html",
        {
            "registerform": registerform,
            "formset": formset,
        },
    )


def RegisterList(request):
    res = Register.objects.all()
    return render(request, "list.html", {"data": res})


class RegisterUpdate(View):
    def get(self, request, *args, **kwargs):
        reg_id = kwargs.get("reg_id")
        reg = get_object_or_404(Register, reg_id=reg_id)
        form = RegisterForm(instance=reg)
        formset = CourseModelFormset(queryset=Courses.objects.filter(course_id=reg))
        return render(request, "edit.html", {"form": form, "formset": formset})

    def post(self, request, *args, **kwargs):
        print("Request POST Data : ", request.POST)
        reg_id = kwargs.get("reg_id")
        reg = get_object_or_404(Register, reg_id=reg_id)
        form = RegisterForm(data=request.POST, instance=reg)
        formset = CourseModelFormset(
            data=request.POST, queryset=Courses.objects.filter(course_id=reg)
        )

        print("before saving :   ", formset.data)
        if form.is_valid() and formset.is_valid():
            print("form is saving ..")
            reg=form.save()
            print("formset is saving ...")
            for form in formset:
                var=form.save(commit=False)
                var.course_id=reg
                var.save()

                # if form.is_valid() and form.cleaned_data:
                #     degree = form.cleaned_data["degree"]
                #     university = form.cleaned_data["university"]
                #     year = form.cleaned_data["year"]
                    # course = Courses.objects.create(
                    #     course_id=reg,
                    #     degree=degree,
                    #     university=university,
                    #     year=year,
                    # )
                    # course.save()
            # instances = formset.save(commit=False)
            # for instance in instances:
            #     instance.save()
            messages.success(request, "Updated successfully")
            return redirect("rlist")
        else:
            print("Form Errors:", form.errors)
            print("Formset Errors:", formset.errors)
            messages.error(request, "Updation failed")
            return render(request, "edit.html", {"form": form, "formset": formset})
        return redirect("rlist")

# class CourseDelete(View):
#     def get(self,request,*args,**kwargs):j
#         id=kwargs.get("id")
#         cd = get_object_or_404(Courses, id=id)  
#         cd.delete()
#         return redirect('ed')

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


# class RegisterUpdate(View):
#     def get(self, request, *args, **kwargs):
#         reg_id = kwargs.get("reg_id")
#         reg = Register.objects.get(reg_id=reg_id)
#         f = RegisterForm(instance=reg)
#         crs = Courses.objects.filter(course_id=reg).first()
#         crs_form = CourseForm(instance=crs)
#         return render(request, "edit.html", {"form": f, "crs_form": crs_form})

#     def post(self, request, *args, **kwargs):
#         reg_id = kwargs.get("reg_id")
#         reg = Register.objects.get(reg_id=reg_id)
#         form_data = RegisterForm(data=request.POST, instance=reg)
#         crs = Courses.objects.filter(course_id=reg).first()
#         crs_form = CourseForm(instance=crs)
#         if form_data.is_valid() and crs_form.is_valid():
#             form_data.save()
#             crs_form.save()
#             messages.success(request, " updated succesfully")
#             return redirect("rlist")
#         else:
#             messages.error(request, "updation failed")
#             return render(
#                 request, "edit.html", {"form": form_data, "crs_form": crs_form}
#             )


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
        formset = CourseModelFormset(data=request.POST, queryset=Courses.objects.filter(course_id=reg))

        print("before saving :   ",formset.data)
        if form.is_valid() and formset.is_valid():
            print("form is saving ..")
            form.save()
            print("formset is saving ...")
            # formset.save()
            instances = formset.save(commit=False)
            for instance in instances:
            # Customize any instance-specific logic if needed
                instance.save()

                print("after saving  : ",form.cleaned_data)
                print(formset.data,"ffff")
                messages.success(request, "Updated successfully")
                return redirect("rlist")
        else:
            print("Form Errors:", form.errors)
            print("Formset Errors:", formset.errors)            
            messages.error(request, "Updation failed")
            return render(request, "edit.html", {"form": form, "formset": formset})
        return redirect('rlist')


# class RegisterUpdate(UpdateView):
#     form_class=CourseModelFormset
#     model=Courses
#     success_url=reverse_lazy("rlist")
#     template_name="edit.html"
#     pk_url_kwarg="pk"
#     def form_valid(self, form):
#         messages.success(self.request,"updated")
#         self.object=form.save()
#         return super().form_valid(form)

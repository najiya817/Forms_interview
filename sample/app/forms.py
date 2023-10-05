from django import forms
from .models import *
from django.forms import formset_factory, modelformset_factory


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["name", "email"]
        widgets = {
            "name": forms.TextInput(
                attrs={"required": True}
            ),
            "email": forms.EmailInput(
                attrs={"class": "custom-email-widget", "required": True}
            ),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ["degree", "university", "year"]
        widgets = {
            "degree": forms.TextInput(attrs={"required": True}),
            "university": forms.TextInput(attrs={"required": True}),
            "year": forms.NumberInput(attrs={"required": True}),
        }


RegisterFormset=formset_factory(RegisterForm,extra=1)
CourseFormset=formset_factory(CourseForm,extra=1)


CourseModelFormset = modelformset_factory(
    Courses,
    fields=(
        "degree",
        "university",
        "year",
    ),
    extra=1,
    widgets={
        "degree": forms.TextInput(
            attrs={"class": "form-control"}
        ),
        "university": forms.TextInput(
            attrs={"class": "form-control"}
        ),
        "year": forms.NumberInput(
            attrs={"class": "form-control"}
        ),
    },
)

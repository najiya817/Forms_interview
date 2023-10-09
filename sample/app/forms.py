from django import forms
from .models import *
from django.forms import formset_factory, modelformset_factory


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ["name", "email"]
        widgets = {
            "name": forms.TextInput(
                attrs={"required": True,"class":"form-control"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "custom-email-widget form-control", "required": True}
            ),
        }
    def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("name")
            email = cleaned_data.get("email")

            # Check for uniqueness of the combination of name and email
            if Register.objects.filter(name=name, email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("A user with this name and email already exists.")

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
    fields=[
         "id",
        "degree",
        "university",
        "year",
    ],
    extra=0,
    widgets={
        'id': forms.HiddenInput(),
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

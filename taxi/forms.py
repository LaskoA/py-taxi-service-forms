from django import forms
from django.core.exceptions import ValidationError

from taxi.models import Driver, Car


def check_license(license_number):
    if len(license_number) != 8:
        raise ValidationError("License number should have 8 symbols")
    elif not license_number[0:3].isalpha():
        raise ValidationError("First 3 symbols should be letters")
    elif not license_number[0:3].isupper():
        raise ValidationError("First 3 letters should be uppercase")
    elif not license_number[3:].isnumeric():
        raise ValidationError("Last 5 symbols should be digits")
    return license_number


class DriverLicenseForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("license_number",)

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        return check_license(license_number)


class DriverCreateForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("first_name", "last_name", "username", "license_number",
                  "email", "is_superuser", "is_staff", "user_permissions")

    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]
        return check_license(license_number)


class CarUpdateForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = "__all__"

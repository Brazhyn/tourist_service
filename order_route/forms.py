from django import forms
from .models import Tourist


class TouristForm(forms.ModelForm):
    class Meta:
        model = Tourist
        fields = '__all__'
        labels = {
            "first_name": "Ім'я",
            "last_name": "Прізвище",
            "age": "Вік",
            "address": "Адреса проживання",
            "phone_number": "Мобільний телефон",
            "email": "Електронна пошта",
            "route": "Маршрут"
        }


class RefuseRouteForm(forms.Form):
    last_name = forms.CharField(label='Прізвище')





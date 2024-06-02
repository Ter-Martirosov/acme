from django import forms
from django.core.exceptions import ValidationError
from .models import Birthday
from django.core.mail import send_mail


BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


class BirthdayForm(forms.ModelForm):

    class Meta:
        model = Birthday
        exclude = ('author', )
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.split()[0]

    def clean(self):
        super().clean()
        # Получаем имя и фамилию из очищенных полей формы.
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        # Проверяем вхождение сочетания имени и фамилии во множество имён.
        if f'{first_name} {last_name}' in BEATLES:
            send_mail(
                subject='Еще один чёрт',
                message=f'{first_name} {last_name} пытался опубликовать запись!',
                from_email='birthday_form@acme.not',
                recipient_list=['admin@acme.not'],
                fail_silently=True,
            )
            raise ValidationError(
                'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
            )

# class BirthdayForm(forms.Form):
#     first_name = forms.CharField(max_length=20, label="Имя")
#     last_name = forms.CharField(required=False, label="Фамилия", help_text='Необязательное поле')
#     birthday = forms.DateField(label="День Рождения", widget=forms.DateInput(attrs={'type': 'date'}))

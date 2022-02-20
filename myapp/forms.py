from django.core.files.storage import FileSystemStorage

from .models import Files, Makets, Nomenklats, Comm
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, NumberInput, CheckboxSelectMultiple, \
    RadioSelect, ChoiceField, FileField, ImageField, ClearableFileInput


class NomenlatsForm(ModelForm):
    class Meta:

        model = Nomenklats
        fields = ['titleNome', 'values', 'quantity', 'plant', 'releases_form', 'country', 'infoNome']


        widgets = {
            "titleNome": TextInput(attrs={
                'placeholder': 'Продукция'
            }),
            "values": NumberInput(attrs={
                'placeholder': 'Объем'
            }),
            "quantity": NumberInput(attrs={
                'placeholder': 'Вложение'
            }),
            "plant": RadioSelect(choices=[('1', 'ЖЛФ'),('2', 'ТЛФ'), ('3', 'БАД')], attrs={
                'blanck': 'True'

            }),
            "releases_form": TextInput(attrs={
                'placeholder': 'Форма выпуска'
            }),
            "country": TextInput(attrs={
                'placeholder': 'Страна'
            }),
            "infoNome": Textarea(attrs={
                'placeholder': 'Описание',

            }),

        }

class MaketsForm(ModelForm):
    class Meta:

        model = Makets
        fields = ['titleMaket', 'typeMaket', 'gregId', 'imgFile', 'infoMaket']

        widgets = {
            "titleMaket": TextInput(attrs={
                'placeholder': 'Название макета',

            }),
            "typeMaket": TextInput(attrs={
                'placeholder': 'Тип макета',
            }),
            "gregId": TextInput(attrs={
                'placeholder': 'Грег макета',
            }),
            "imgFile": ClearableFileInput(attrs={
                'multiple': 'True'
            }),
            "infoMaket": Textarea(attrs={
                'placeholder': 'Описание'
            })

        }


class FilesForm(ModelForm):
    class Meta:

        model = Files
        fields = ['titleFile', 'locsave']

        widgets = {

        }


class CommForm(ModelForm):
    class Meta:

        model = Comm
        fields = ['whoMakets', 'whoNomenklats', 'aktuality']

        widgets = {
            "whoMakets": TextInput(attrs={
                'label': 'Макет',
                'placeholder': 'Выберите макет'
            }),
            "whoNomenklats": TextInput(attrs={
                'placeholder': 'Выберите номенклатуру',
                'id_whoMakets': 'Макеты',
                'request_name': 'Макеты'
            })

        }
from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_current':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    # Наследуемся от специального класса форм, который предоставляет
    # весь необходимый функционал, который нужно настроить
    black_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product  # Обязательно указываем модель
        exclude = ('date_of_creation ', 'last_modified_date')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         if field_name != 'is_current':
    #             field.widget.attrs['class'] = 'form-control'

    #         field.help_text = 'Some help text for field'

    def clean_name(self):

        cleaned_data = self.cleaned_data.get('name')

        for word in self.black_list:
            if word in cleaned_data:
                raise forms.ValidationError('Name of product has forbidden words!')

        return cleaned_data

    def clean_description(self):

        cleaned_data = self.cleaned_data.get('description')

        for word in self.black_list:
            if word in cleaned_data:
                raise forms.ValidationError('Description has forbidden words!')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name, field in self.fields.items():
    #         if field_name != 'is_current':
    #             field.widget.attrs['class'] = 'form-control'

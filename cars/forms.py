from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = ('__all__')

    def clean_value(self):
        VALOR_MINIMO = 20000
        value = self.cleaned_data.get('value')
        if value < VALOR_MINIMO:
            self.add_error('value', f'valor mínimo do carro deve ser de R${VALOR_MINIMO},00.')
        return value
    
    def clean_factory_year(self):
        ANO_MINIMO = 1975
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < ANO_MINIMO:
            self.add_error('factory_year', f'Data excedeu o ano mínimo de {ANO_MINIMO}.')
        return factory_year

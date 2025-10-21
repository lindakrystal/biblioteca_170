from django import forms
from datetime import date
from rut_chile import rut_chile
from .models import Lector


class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = '__all__'

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        digito = self.cleaned_data.get('digito_verificador')

        rut_completo = f"{rut}-{digito}".upper()
        if not rut_chile.is_valid_rut(rut_completo):
            raise forms.ValidationError("❌ El RUT ingresado no es válido.")
        return rut

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha > date.today():
            raise forms.ValidationError("❌ La fecha de nacimiento no puede ser en el futuro.")
        return fecha

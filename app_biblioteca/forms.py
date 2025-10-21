from django import forms
from datetime import date
from .models import Lector, validar_rut_chileno

class LectorForm(forms.ModelForm):
    class Meta:
        model = Lector
        fields = '__all__'
        labels = {
            'rut': 'RUT',
            'fecha_nacimiento': 'Fecha de Nacimiento',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        # Validación usando la función que ya definimos en el modelo
        try:
            validar_rut_chileno(rut)
        except forms.ValidationError as e:
            raise forms.ValidationError(f"❌ {e}")
        return rut

    def clean_fecha_nacimiento(self):
        fecha = self.cleaned_data.get('fecha_nacimiento')
        if fecha > date.today():
            raise forms.ValidationError("❌ La fecha de nacimiento no puede ser en el futuro.")
        # Validar edad mínima (5 años)
        edad = date.today().year - fecha.year - ((date.today().month, date.today().day) < (fecha.month, fecha.day))
        if edad < 5:
            raise forms.ValidationError("❌ El lector debe tener al menos 5 años de edad.")
        return fecha

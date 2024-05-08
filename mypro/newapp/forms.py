from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['tanggal', 'jumlah', 'sumber', 'deskripsi']  # Field yang akan dimasukkan dalam form
